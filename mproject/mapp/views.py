import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TeacherReg, TeacherLog, StudentReg # StudentLog #EnrollForm #AuthorityLogForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Teacher,Student

# from .models import Admin

# from django.contrib.auth import authenticate, login

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def admin(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())


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
    student_data = list(students.values('firstname', 'lastname', 'admission_number'))
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
            Password = form.cleaned_data['password']
            
            teacherd = Teacher.objects.filter(username=username).first()
            
            if teacherd and teacherd.Password == Password:
                request.session['role'] = 'Teacher'
                request.session['teacher_id'] = teacherd.id
                messages.success(request, 'Login successful')
                return redirect('teacher')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = TeacherLog()
        
    return render(request, 'teacher_log.html', {'form': form})



def teacher(request):

    teacher_id = request.session.get('user_id')
    if not teacher_id:
        return redirect('teacher_log')    

    teacher = Teacher.objects.get(id=teacher_id)

    
    return render(request, 'teacherboard.html', {'teacher': teacher})

def student(request):

    student_id = request.session.get('user_id')
    if not student_id:
        return redirect('teacher_log')    

    teacher = Teacher.objects.get(id=student_id)

    
    return render(request, 'studentboard.html', {'teacher': teacher})


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
# def authority_login(request):
#     template = loader.get_template('authority_login.html')
#     return HttpResponse(template.render())

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



# def authority_login(request):
#     form = AuthorityLogForm()
#     if request.method == 'POST':
#         form = AuthorityLogForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')  # Redirect to a success page
#             else:
#                 form.add_error(None, 'Invalid username or password')
#     context = {'loginform': form}
#     return render(request, 'login.html', context=context)


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
#             teacher_user = Teacher.objects.filter(username=username).first()
#             if teacher_user and teacher_user.Password == Password:  # Replace with hashed password check if necessary
#                 # Store the teacher's role and ID in the session
#                 request.session['role'] = 'Teacher'
#                 request.session['user_id'] = teacher_user.id
#                 messages.success(request, 'Login successful!')
#                 return redirect('teacher')  # Redirect to the teacher's dashboard
#             else:
#                 messages.error(request, 'Invalid username or password')
#     else:
#         form = TeacherLog()  # Render an empty login form for GET requests
        
#     return render(request, 'teacher_log.html', {'form': form})