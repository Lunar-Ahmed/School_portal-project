import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TeacherReg,  StudentReg,TeacherLog, StudentLog #EnrollForm #AuthorityLogForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Teacher,Student

# from .models import Admin

# from django.contrib.auth import authenticate, login

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def admin(request):
    # departments = Department.objects.all()
    return render(request, 'base.html')


def student(request):
    template = loader.get_template('studentboard.html')
    return HttpResponse(template.render())

def bursar(request):
    template = loader.get_template('bursar.html')
    return HttpResponse(template.render())

def assignment(request):
    template = loader.get_template('attendance.html')
    return HttpResponse(template.render())



def acad(request):
    teacher_data = Teacher.objects.all().values
    template = loader.get_template('acad_dashboard.html')
    context = {
        'teacher_data': teacher_data,    
    }
    return HttpResponse(template.render(context, request))


from django.http import JsonResponse
def get_students_by_class(request, class_level):
    students = Student.objects.filter(class_level=class_level)
    student_data = list(students.values('id', 'firstname', 'lastname', 'admission_number'))
    return JsonResponse(student_data, safe=False)




# def get_students_by_class(request, class_level):
#     students = Student.objects.filter(class_level=class_level)
#     context = {
#         'students': students,
#         'class_level': class_level
#     }
#     return render(request, 'acad_dashboard.html', context)
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Teacher

def toggle_teacher_status(request, teacher_id):
    if request.method == "POST":
        teacher = get_object_or_404(Teacher, id=teacher_id)
        teacher.is_active = not teacher.is_active  # Toggle the status
        teacher.save()
        status = "enabled" if teacher.is_active else "disabled"
        messages.success(request, f"Teacher account has been {status}.")
    return redirect('acad')  # Replace 'teacher_list' with the URL name of your teacher management page





from django.shortcuts import render
from .models import StudentScore

def student_scores(request):
    students = Teacher.objects.all()  # Get all students and their scores
    return render(request, 'testing.html', {'students': students})


# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import StudentScore

@csrf_exempt
def update_scores(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_id = data['student_id']
        ca1 = float(data['ca1'])
        ca2 = float(data['ca2'])
        ca3 = float(data['ca3'])

        student = StudentScore.objects.get(id=student_id)
        student.ca1 = ca1
        student.ca2 = ca2
        student.ca3 = ca3
        student.calculate_total()  # Recalculate total

        return JsonResponse({'success': True, 'total': student.total})
    return JsonResponse({'success': False})



#================REGISTERATION================
def teacher_register(request):
    if request.method == 'POST':
        form = TeacherReg(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            return redirect('acad')  # Redirect to a success page
    else:
        form = TeacherReg()
    
    return render(request, 'teacher_reg.html', {'form': form})

def teacher_login(request):
    if request.method == 'POST':
        form = TeacherLog(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['Password']
            
            # Get the teacher by username
            teacherd = Teacher.objects.filter(username=username).first()
            
            if teacherd:
                if not teacherd.is_active:
                    messages.error(request, 'Your account is disabled. Please contact the admin.')
                    return render(request, 'teacher_log.html', {'form': form})
                
                # Verify password (you may need to hash passwords if not already done)
                if teacherd.Password == password:  # Replace with hashed check if passwords are hashed
                    request.session['role'] = 'Teacher'
                    request.session['user_id'] = teacherd.id
                    messages.success(request, 'Login successful')
                    return redirect('teacher')
                else:
                    messages.error(request, 'Invalid username or password')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = TeacherLog()
        
    return render(request, 'teacher_log.html', {'form': form})



    students = Student.objects.all()


    # Define the range of weeks and days
    weeks = list(range(1, 14))  # Weeks 1 to 13
    days = list(range(1, 6))    # Days 1 to 5

    if request.method == 'POST':
        # Handle form submission (if applicable)
        pass

    # Pass the data to the template
    return render(request, 'teacherboard.html', {
        'students': students,
        'weeks': weeks,
        'days': days,
    })




from django.shortcuts import render, redirect
from .models import InputTable # Ensure Teacher model is imported
from .forms import InputTableForm

def table_view(request):
    # Fetch all teacher names
    teachers = Teacher.objects.all().values()
    input_table = InputTable.objects.first()  # Get the first record
    if not input_table:
        input_table = InputTable.objects.create()

    if request.method == 'POST':
        form = InputTableForm(request.POST, instance=input_table)
        if form.is_valid():
            form.save()
            return redirect('table_view')
    else:
        form = InputTableForm(instance=input_table)

    context = {
        'form': form,
        'total': input_table.total(),
        'teachers': teachers,
    }

    return render(request, 'teacherboard.html', context)



#===============main Teacher board==================
from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher, Student, Subject

def teacher(request):
    teacher_id = request.session.get('user_id')
    if not teacher_id:
        return redirect('teacher_log')

    # Retrieve teacher's information
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    # Get the subject that the teacher is teaching
    selected_subject = teacher.Subject_Teacher

    # Find the subject instance from the database
    subject_instance = Subject.objects.filter(name=selected_subject).first()

    if subject_instance:
        # Fetch students who are enrolled in this subject
        students = Student.objects.filter(subjects=subject_instance)
    else:
        students = []

    # Handle the teacher's form for updating their profile
    if request.method == 'POST':
        teacher.username = request.POST.get('username')
        teacher.email = request.POST.get('email')
        
        password = request.POST.get('password')
        if password:
            teacher.set_password(password)
        
        if 'profile_picture' in request.FILES:
            teacher.profile_picture = request.FILES['profile_picture']
        
        teacher.save()
        return redirect('teacher')

    # Weeks and days for the teacher's schedule or other context
    weeks = list(range(1, 14))
    days = list(range(1, 6))

    return render(request, 'teacherboard.html', {
        'teacher': teacher,
        'students': students,
        'weeks': weeks,
        'days': days,
        'selected_subject': selected_subject,
    })


# def teacher(request):
#     # students = Student.objects.all()

#     # Get the teacher's selected subject
#     selected_subject = teacher.Subject_Teacher

#     # Fetch the corresponding Subject instance
#     subject_instance = Subject.objects.filter(name__icontains=selected_subject).first()

#     # Ensure subject_instance exists to avoid errors
#     if subject_instance:
#         # Filter students based on subjects offered
#         students = Student.objects.filter(subjects=subject_instance)
#     else:
#         students = []
    
#         # Get the logged-in teacher
#     teacher_id = request.session.get('user_id')  # Assuming `user_id` is stored in the session during login
#     teacher = get_object_or_404(Teacher, id=teacher_id)
    
#     if request.method == 'POST':
#         teacher.username = request.POST.get('username')
#         teacher.email = request.POST.get('email')
#         password = request.POST.get('password')

#         if password:
#             teacher.set_password(password)  # Update password if provided
        
#         if 'profile_picture' in request.FILES:
#             teacher.profile_picture = request.FILES['profile_picture']
        
#         teacher.save()
#         return redirect('teacher')

#     # Get students of the teacher's assigned class
#     students = Student.objects.filter(class_level=teacher.Class_Teacher)

#     # Define the range of weeks and days
#     weeks = list(range(1, 14))  # Weeks 1 to 13
#     days = list(range(1, 6))    # Days 1 to 5

#     if request.method == 'POST':
#         # Handle form submission (if applicable)
#         pass

#     # Pass the data to the template

#     teacher_id = request.session.get('user_id')
#     if not teacher_id:
#         return redirect('teacher_log')    

#     teacher = Teacher.objects.get(id=teacher_id)
    
#     return render(request, 'teacherboard.html', {'teacher': teacher, 'students':students, 'weeks': weeks, 'days': days, 'students': students, 'selected_subject': selected_subject,})

from django.shortcuts import render
from .models import Teacher, Student, Subject

# def teacher(request):
#     # Fetch the logged-in teacher
#     teacher = Teacher.objects.get(username=request.user.username)

#     # Get the teacher's selected subject
#     selected_subject = teacher.Subject_Teacher

#     # Fetch the corresponding Subject instance
#     subject_instance = Subject.objects.filter(name__icontains=selected_subject).first()

#     # Ensure subject_instance exists to avoid errors
#     if subject_instance:
#         # Filter students based on subjects offered
#         students = Student.objects.filter(subjects=subject_instance)
#     else:
#         students = []

#     context = {
#         'teacher': teacher,
#         'students': students,
#         'selected_subject': selected_subject,
#     }
#     return render(request, 'teacherboard.html', context)



def teacher_details(request, teacher_id):
    teacher= get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_details_partial.html', {'teacher': teacher})

def update_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    if request.method == 'POST':
        teacher.Firstname = request.POST['Firstname']
        teacher.Middlename = request.POST['Middlename']
        teacher.Lastname = request.POST['Lastname']
        teacher.Email = request.POST['Email']
        teacher.Mobile = request.POST['Mobile']
        teacher.Address = request.POST['Address']
        teacher.save()
        return redirect('acad')


def student(request):

    student_id = request.session.get('user_id')
    if not student_id:
        return redirect('teacher_log')    

    teacher = Teacher.objects.get(id=student_id)

    
    return render(request, 'studentboard.html', {'teacher': teacher})


def student_details(request, student_id):
    student= get_object_or_404(Student, id=student_id)
    return render(request, 'student_details_partial.html', {'student': student})

def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.firstname = request.POST['firstname']
        student.middlename = request.POST['middlename']
        student.lastname = request.POST['lastname']
        student.username= request.POST['username']
        student.mobile = request.POST['mobile']
        student.address = request.POST['address']
        student.save()
        return redirect('acad')
    
    
def student_login(request):
    form = StudentLog()
    if request.method == 'POST':
        form = StudentLog(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('student')  # Redirect to a success page
            else:
                form.add_error(None, 'Invalid username or password')
    context = {'form': form}
    return render(request, 'student_login.html', context=context)


def student_register(request):
    if request.method == 'POST':
        form = StudentReg(request.POST, request.FILES)
        if form.is_valid():
            student = form.save()  # Save the student object
            # No need for manual creation of class models, the `save` method on the `Student` model will handle it.
            return redirect('acad')  # Redirect to a success page
        else:
            return HttpResponse("Form is not valid.")
    else:
        form = StudentReg()
    
    return render(request, 'student_register.html', {'form': form})




def attendance_view(request):
    # Fetch all students
    students = Student.objects.all()


    # Define the range of weeks and days
    weeks = list(range(1, 14))  # Weeks 1 to 13
    days = list(range(1, 6))    # Days 1 to 5

    if request.method == 'POST':
        # Handle form submission (if applicable)
        pass

    # Pass the data to the template
    return render(request, 'teacherboard.html', {
        'students': students,
        'weeks': weeks,
        'days': days,
    })


# from .models import Subject
# from .forms import SubjectForm
# # views.py
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import Department, Subject
# import json
# # Fetch subjects based on department
# def fetch_department_subjects(request):
#     if request.method == "GET":
#         department_name = request.GET.get('department')
#         department = Department.objects.get(name=department_name)
#         subjects = department.subjects.all()
#         subject_list = [{"id": subject.id, "name": subject.name} for subject in subjects]
#         return JsonResponse({"subjects": subject_list})

# # Add a new subject
# @csrf_exempt
# def add_subject(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         department_name = data.get("department")
#         subject_name = data.get("subject_name")
#         department = Department.objects.get(name=department_name)
#         Subject.objects.create(name=subject_name, department=department)
#         return JsonResponse({"success": True, "message": "Subject added successfully"})

# # Delete a subject
# @csrf_exempt
# def delete_subject(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         subject_id = data.get("subject_id")
#         Subject.objects.get(id=subject_id).delete()
#         return JsonResponse({"success": True, "message": "Subject deleted successfully"})





#=======Teacher update profile===========
# def teacher_update(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id)

#     if request.method == 'POST':
#         teacher.username = request.POST.get('username')
#         teacher.email = request.POST.get('email')
#         password = request.POST.get('password')

#         if password:
#             teacher.set_password(password)  # Update password if provided
        
#         if 'profile_picture' in request.FILES:
#             teacher.profile_picture = request.FILES['profile_picture']
        
#         teacher.save()
#         return redirect('teacher')  # Redirect to the teacher's dashboard or profile page

#     return render(request, 'teacherboard.html', {'teacher': teacher})

# from django.shortcuts import render, get_object_or_404, redirect
# from .models import Student, Attendance
# from .forms import AttendanceForm

# def attendance_view(request, student_id, week):
#     student = get_object_or_404(Student, id=student_id)
#     attendance, created = Attendance.objects.get_or_create(student=student, week=week)
#     if request.method == 'POST':
#         form = AttendanceForm(request.POST, instance=attendance)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher', student_id=student_id, week=week)
#     else:
#         form = AttendanceForm(instance=attendance)
#     return render(request, 'teacher_dashboard.html', {'form': form, 'student': student, 'week': week})




# 




# def authority_login(request):
#     form = AuthorityLogForm()
#     if request.method == 'POST':
#         form = AuthorityLogForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data['email']
#             department = form.cleaned_data['department']
#             password = form.cleaned_data['password']
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 if department == 'A':
#                     return redirect('admin')
#                 elif department == 'T':
#                     return redirect('teacher')
#                 elif department == 'B':
#                     return redirect('bursar')
#             # else:
#             #     form.add_error(None, 'Invalid email, department, or password')
#     # context = {'loginform': form}
#     return render(request, 'authority_login.html',{'form': form}) #context=context)


# def admin_register(request):
#     form = AdminRegForm()
#     if request.method == 'POST':
#         form = Reg(request.POST)
#         if form.is_valid(): 
#             form.save()
#             return redirect('login')
#     context = {'registerform': form}
#     # else:
#     #     form = RegistrationForm()
#     return render(request, 'regform.html', context=context)# {'context': form})



#===============LOGINS========================

# def student_login(request):
#     if request.method == 'POST':
#         form = StudentLog(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             Password = form.cleaned_data['Password']
            
#             teacherd = Student.objects.filter(username=username).first()
            
#             if teacherd and teacherd.Password == Password:
#                 request.session['role'] = 'Student'
#                 request.session['user_id'] = teacherd.id
#                 messages.success(request, 'Login successful')
#                 return redirect('student')
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = StudentLog()
        
#     return render(request, 'student_login.html', {'form': form})
# def admin_login(request):
#     if request.method == 'POST':
#         form = AdminLogin(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#         admin_log = admin.objects.filter(username=username, password=password).first()
#         if admin_log:
#             request.session['role'] = 'Admin'
#             request.session['user_id'] = admin_log.id
#             return redirect('admin')
#         else:
#             form = AdminLogin()
#             return render(request, 'admin_log.html', {'form': form})
# def admin_login(request):
#     if request.method == 'POST':
#         form = AdminLogin(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             admin_log = Admin.objects.filter(username=username, password=password).first()
#             if admin_log:
#                 request.session['role'] = 'Admin'
#                 request.session['user_id'] = admin_log.id
#                 return redirect('admin')
#         else:
#             form.add_error(None, 'Invalid username or password') 
#     else:
#         form = AdminLogin()
    
#     return render(request, 'admin_log.html', {'form': form})






# views.py
# from django.shortcuts import redirect, get_object_or_404
# from .models import Teacher

# def toggle_teacher_status(request, teacher_id):
#     teacher = get_object_or_404(Teacher, id=teacher_id)

#     # Toggle the status
#     teacher.is_disabled = not teacher.is_disabled
#     teacher.save()

#     # You can also disable or enable the corresponding User model if necessary:
#     if teacher.user:
#         teacher.user.is_active = not teacher.is_disabled
#         teacher.user.save()

#     return redirect('acad')  # Redirect back to the teacher list page







# def class_cards(request):
#     # Get all students and class levels
#     class_levels = ['jss1', 'jss2', 'jss3', 'ss1', 'ss2', 'ss3']
#     students = Student.objects.all()
#     return render(request, 'adcad_dashboard.html', {
#         'class_levels': class_levels,
#         'students': students
#     })


# def class_students(request, class_level):
#     # Render students in the selected class_level
#     students = Student.objects.filter(class_level=class_level)
#     return render(request, 'acad_dashboard.html', {'students': students, 'class_level': class_level})


# def teacher_login(request):
#     if request.method == 'POST':
#         form = TeacherLog(request.POST)  # Use the LoginForm for authentication
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             Password = form.cleaned_data['Password']
            
#             # Fetch the teacher by username and check the password
#             teacherd = Teacher.objects.filter(username=username).first()
#             if teacherd and teacherd.Password == Password:  # Replace with hashed password check if necessary
#                 # Store the teacher's role and ID in the session
#                 request.session['role'] = 'Teacher'
#                 request.session['teacher_id'] = teacherd.id
#                 messages.success(request, 'Login successful!')
#                 return redirect('teacher')  # Redirect to the teacher's dashboard
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = TeacherLog()  # Render an empty login form for GET requests
        
#     return render(request, 'teacher_log.html', {'form': form})




# def enroll_form(request):
#     form = EnrollForm()
#     if request.method == 'POST':
#         form = EnrollForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('')
#     # else:
#     #     form = UserRegistrationForm()
#     return render(request, 'enroll_register.html', {'form': form})