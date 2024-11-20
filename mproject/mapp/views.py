from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import TeacherReg, StudentRegForm, EnrollForm,AdminLogin #AuthorityLogForm 
from django.contrib.auth import authenticate, login
# from .models import Admin

# from django.contrib.auth import authenticate, login

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def admin(request):
    template = loader.get_template('base.html')
    return HttpResponse(template.render())

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

def enroll_form(request):
    form = EnrollForm()
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    # else:
    #     form = UserRegistrationForm()
    return render(request, 'enroll_register.html', {'form': form})


def teacher_register(request):
    form = TeacherReg()
    if request.method == 'POST':
        form = TeacherReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher')
    # else:
    #     form = UserRegistrationForm()
    return render(request, 'teacher_register.html', {'form': form})


def student_register(request):
    form = StudentRegForm()
    if request.method == 'POST':
        form = StudentRegForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_login')
    # else:
    #     form = UserRegistrationForm()
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