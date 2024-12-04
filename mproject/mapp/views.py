from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TeacherReg, TeacherLog #StudentRegForm, EnrollForm #AuthorityLogForm 
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Teacher 

# from .models import Admin

# from django.contrib.auth import authenticate, login

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def admin(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

# def teacher(request):
#     teachd = Teacher.objects.all().values()
#     template = loader.get_template('teacherboard.html')
#     context = {
#         'teachd': teachd,
#     }
#     return HttpResponse(template.render(context, request)
# def teacher(request, Username):
#     teachd = Teacher.objects.get(Username=Username)
#     template = loader.get_template('teacherboard.html')
#     context = {
#         'teachd': teachd,
#     }
#     return HttpResponse(template.render(context, request))





def teacher(request):
    template = loader.get_template('teacherboard.html')
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
    template = loader.get_template('acad_dashboard.html')
    return HttpResponse(template.render())

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


# def teacher_register(request):
#     form = TeacherReg()
#     if request.method == 'POST':
#         form = TeacherReg(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('teacher')
#     # else:
#     #     form = UserRegistrationForm()
#     return render(request, 'teacher_reg.html', {'form': form})

def teacher_register(request):
    if request.method == 'POST':
        form = TeacherReg(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # This will save the form data to the database
            return redirect('teacher_login')  # Redirect to a success page
    else:
        form = TeacherReg()
    
    return render(request, 'teacher_reg.html', {'form': form})



def teacher_login(request):
    if request.method == 'POST':
        form = TeacherLog(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            Password = form.cleaned_data['Password']
            
            teacherd = Teacher.objects.filter(username=username).first()
            
            if teacherd and teacherd.Password == Password:
                request.session['role'] = 'Teacher'
                request.session['user_id'] = teacherd.id
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






# def student_register(request):
#     form = StudentRegForm()
#     if request.method == 'POST':
#         form = StudentRegForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('student_login')
#     # else:
#     #     form = UserRegistrationForm()
#     return render(request, 'student_register.html', {'form': form})


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

def student_login(request):
    template = loader.get_template('student_login.html')
    return HttpResponse(template.render())

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