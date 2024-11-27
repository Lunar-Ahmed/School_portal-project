from django import forms
from .models import Teacher, Tlogin#Student, Enroll
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


class TeacherLog(forms.ModelForm):
    class Meta:
        model = Tlogin
        fields = ['Username', 'Password']


        
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