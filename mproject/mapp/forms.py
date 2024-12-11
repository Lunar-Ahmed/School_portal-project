from django import forms
from .models import Teacher, Student # Enroll
from django.contrib.auth.forms import AuthenticationForm

class TeacherReg(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
        widgets = {
            'DOB': forms.DateInput(attrs={'type': 'date'}),
            'Gender': forms.Select,
            'Subject_Teacher': forms.Select(attrs={'placeholder': 'Choose Subject'}),
            'Class_Teacher': forms.Select
        }
class StudentReg(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select,
        }


class TeacherLog(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['username', 'Password']
        
        
from django.contrib.auth.backends import BaseBackend
from django.db import connections
from django.contrib.auth.hashers import check_password
from .models import Teacher  # Replace with your app name

# from .models import Attendance

# class AttendanceForm(forms.ModelForm):
#     class Meta:
#         model = Attendance
#         fields = ['day1', 'day2', 'day3', 'day4', 'day5']

        
# class StudentLog(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['username', 'password']


from .models import InputTable

class InputTableForm(forms.ModelForm):
    class Meta:
        model = InputTable
        fields = ['input1', 'input2', 'input3']


        
# class StudentRegForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ['Profile_Picture', 'Firstname', 'Middlename', 'Lastname', 'username', 'Mobile', 'Department', 'Parent_Mobile', 'Address', 'Gender', 'Class', 'DOB', 'Email', 'Admission_Number', 'Password']
#         widgets = {
#             'DOB': forms.DateInput(attrs={'type': 'date'}),
#             'Gender': forms.Select,
#             'Department': forms.Select,
#             'Class': forms.Select
#         }
        
# class EnrollForm(forms.ModelForm):
#     class Meta:
#         model : Enroll
#         fields = ['student_name', 'parent-phone', 'email', 'address', 'message']
            
# class AdminLogin(forms.Form):
#     username = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)
    

        
# class AuthorityLogForm(forms.Form):
#     email = forms.EmailField(max_length=100)
#     DEPARTMENT_CHOICES = [
#         ('A', 'Admin'),
#         ('T', 'Teacher'),
#         ('B', 'Bursar'),
#     ]
#     department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
#     password = forms.CharField(widget=forms.PasswordInput)
    

# class StudentLogForm(forms.Form):
#     username = forms.CharField(max_length=255)
#     CLASS_CHOICES = [
#         ('j1', 'Jss1'),
#         ('j2', 'Jss2'),
#         ('j3', 'Jss3'),
#         ('s1', 'Ss1'),
#         ('s2', 'Ss2'),
#         ('s3', 'Ss3'),
#     ]
#     classs = forms.CharField(choices=CLASS_CHOICES)
#     password = forms.CharField(widget=forms.PasswordInput)
        
# class AuthorityLogForm(forms.Form):
#     email = forms.CharField(max_length=100)
#     password = forms.CharField(widget=forms.PasswordInput)