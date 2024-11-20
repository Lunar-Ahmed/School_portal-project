from django import forms
from .models import Student, Enroll, Teacher


class TeacherReg(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['Profile','Firstname', 'Middlename','Lastname', 'Mobile', 'Address', 'Sex', 'Emergency', 'Class', 'Subject', 'DOB', 'Cv','Email', 'Password']
        
class StudentRegForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['fullname','username','schoolNo', 'state',  'DOB', 'address', 'phone', 'parent_phone', 'classs',  'email', 'password']
        
class EnrollForm(forms.ModelForm):
    class Meta:
        model : Enroll
        fields = ['student_name', 'parent-phone', 'email', 'address', 'message']
            
class AdminLogin(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    

        
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