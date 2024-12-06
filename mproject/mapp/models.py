from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# class Enroll(models.Model):
#     student_name = models.CharField(max_length=50)
#     parent_phone = models.CharField(max_length=50)
#     email = models.IntegerField()
#     address = models.EmailField(max_length=100)
#     Message = models.TextField(max_length=150)
    
# class Teacher(AbstractUser):
#     CLASS_CHOICES =[
#         ('class_teacher', 'Class Teacher'),
#         ('teacher', 'Teacher'),
#     ]
   
# class Attendance(models.Model):
#     class_name = models.CharField(max_length=100, choices=Teacher.CLASS_CHOICES)
#     student_name = models.CharField(max_length=150)
#     week_1 = models.BooleanField(default=False)
#     week_2 = models.BooleanField(default=False)
#     week_3 = models.BooleanField(default=False)
#     week_4 = models.BooleanField(default=False)
#     week_5 = models.BooleanField(default=False)
#     week_6 = models.BooleanField(default=False)
#     week_7 = models.BooleanField(default=False)
#     week_8 = models.BooleanField(default=False)
#     week_9 = models.BooleanField(default=False)
#     week_10 = models.BooleanField(default=False)
#     week_11 = models.BooleanField(default=False)
#     week_12 = models.BooleanField(default=False)
#     week_13 = models.BooleanField(default=False)
#     week_14 = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.class_name} - {self.student_name}"
   

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = [ ('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ]
    SUBJECT_CHOICES = [ ('M', 'Mathematics(general)'), ('E', 'English(general)'), ('C', 'Civic(general)'), ('B', 'Biology(general)'), ('CH', 'Chemistry(science)'), ('PY', 'Physics(civic)'), ('DP', 'Data-Processing(general)'), ('MK', 'Marketing(commercial)'), ('EC', 'Economic(general)'), ('COM', 'Computer-Studies(general)'), ('FM', 'Further-Math(science)'), ('GV', 'Government(art, commercial)'), ('LT', 'Literature(art)'), ('CM', 'Commerce(commercial)'), ('Ac', 'Accounting(commercial)'), ('HS', 'History(art)'), ('GG', 'Geography(science)'), ('C', 'Book-Keeping(science)'),  ('Is', 'Islamic-Studies(general)'), ('Chr', 'Christain-Studies(general)'), ('TD', 'Technical-Drawing(science)'),]
    CLASS_CHOICES = [ ('J1', 'Jss1'), ('J2', 'Jss2'), ('J3', 'Js3'), ('S1', 'Ss1'), ('S2', 'Ss2'), ('S3', 'Ss3'), ]
    DEPARTMENT_CHOICES = [('Sc', 'Science'), ('Ar', 'Art'), ('Cm', 'Commercial'), ]
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    Firstname = models.CharField(max_length=150, null=True)
    Middlename = models.CharField(max_length=150, null=True)
    Lastname = models.CharField(max_length=150, null=True)
    Mobile = models.CharField(null=True, max_length=50)
    username = models.CharField(null=True, max_length=50)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Address = models.CharField(max_length=150, null=True)
    Emergency = models.CharField(null=True, max_length=50)
    Subject_Teacher = models.CharField(max_length=5, choices=SUBJECT_CHOICES)
    Class_Teacher =  models.CharField(max_length=5, choices=CLASS_CHOICES)
    DOB= models.DateTimeField()
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=150) 
    Cv = models.FileField(upload_to='documents/', null=True)
    is_disabled = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"
    
    
# from django.contrib.auth.backends import ModelBackend
# from django.contrib.auth import get_user_model

# class CustomBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         User = get_user_model()
#         try:
#             user = User.objects.get(username=username)
#             if user.check_password(password) and not user.is_disabled:
#                 return user
#         except User.DoesNotExist:
#             return None
        
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class CustomBackend(ModelBackend):
    def user_can_authenticate(self, user):
        is_active = getattr(user, 'is_active', None)
        return is_active or is_active is None


    
    
# class Student(models.Model):
#     GENDER_CHOICES = [ 
#         ('M', 'Male'), 
#         ('F', 'Female'),
#         ('O', 'Other'), 
#         ]
#     DEPARTMENT_CHOICES = [ 
#         ('S', 'Science'), 
#         ('A', 'Art'),
#         ('C', 'Commercial'), 
#         ]
#     CLASS_CHOICES = [ 
#         ('J1', 'JsS1'), 
#         ('J2', 'Jss2'),
#         ('J3', 'Jss3'), 
#         ('S1', 'SS1'), 
#         ('S2', 'Ss2'),
#         ('S3', 'Ss3'), 
#         ]
#     Profile_Picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
#     Firstname = models.CharField(max_length=150, null=True)
#     Middlename = models.CharField(max_length=150, null=True)
#     Lastname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=250)
#     Mobile = models.IntegerField(null=True)
#     Department = models.CharField(max_length=5, choices=DEPARTMENT_CHOICES)
#     Parent_Mobile = models.IntegerField()
#     Address = models.CharField(max_length=150, null=True)
#     Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
#     Class =  models.CharField(max_length=5, choices=CLASS_CHOICES)
#     DOB= models.DateTimeField()
#     Email = models.EmailField(max_length=100)
#     Admission_Number = models.CharField(max_length=150)
#     Password = models.CharField(max_length=150)  

    
    
    
# class Admin(models.Model):
#     fullname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=150, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)
#     department = models.CharField(max_length=50)

# class Teacher(models.Model):
#     Firstname = models.CharField(max_length=150, null=True)
#     Middlename = models.CharField(max_length=150, null=True)
#     Lastname = models.CharField(max_length=150, null=True)
#     Mobile = models.IntegerField(max_length=150, null=True)
#     Address = models.CharField(max_length=150, null=True)
#     Sex = models.CharField(max_length=150, null=True)
#     Emargency = models.IntegerField(max_length=150, null=True)
#     Class_Teacher =  models.CharField(max_length=150, null=True)
#     Subject_Teacher= models.CharField(max_length=150, null=True)
#     DOB= models.BigIntegerField()
#     Email = models.EmailField(max_length=100)
#     Password = models.CharField(max_length=150)


# class Bursar(models.Model):
#     fullname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=150, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)
#     department = models.CharField(max_length=50)

# class Admin(models.Model):
#     fullname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=150, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)
#     department = models.CharField(max_length=50)

# class Teacher(models.Model):
#     fullname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=150, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)
#     department = models.CharField(max_length=50)

# class Bursar(models.Model):
#     fullname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=150, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)
#     department = models.CharField(max_length=50)

# class Authority(models.Model):
#     DEPARTMENT_CHOICES = [
#         ('A', 'Admin'),
#         ('T', 'Teacher'),
#         ('B', 'Bursar'),
#     ]
#     fullname = models.CharField(max_length=150, null=True)
#     username = models.CharField(max_length=150, null=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField(max_length=100)
#     department = models.CharField(max_length=1, choices=DEPARTMENT_CHOICES)
#     password = models.CharField(max_length=150)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.department == 'A':
#             Admin.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 phone=self.phone,
#                 email=self.email,
#                 password=self.password,
#                 department='Admin'
#             )
#         elif self.department == 'T':
#             Teacher.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 phone=self.phone,
#                 email=self.email,
#                 password=self.password,
#                 department='Teacher'
#             )
#         elif self.department == 'B':
#             Bursar.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 phone=self.phone,
#                 email=self.email,
#                 password=self.password,
#                 department='Bursar'
#             )

#===========================================================================

# class Jss1(models.Model):
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=40)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

# class Jss2(models.Model):
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=40)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

# class Jss3(models.Model):
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=40)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

# class Ss1(models.Model):
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=40)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

# class Ss2(models.Model):
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=40)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

# class Ss3(models.Model):
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=40)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

# class Student(models.Model):
#     CLASS_CHOICES = [
#         ('j1', 'Jss1'),  
#         ('j2', 'Jss2'),
#         ('j3', 'Jss3'),
#         ('s1', 'Ss1'),
#         ('s2', 'Ss2'),
#         ('s3', 'Ss3'),
#     ]
#     fullname = models.CharField(max_length=350)
#     username = models.CharField(max_length=100)
#     schoolNo = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     LGA = models.CharField(max_length=100)
#     DOB = models.CharField(max_length=50)
#     address = models.CharField(max_length=200)
#     phone = models.BigIntegerField()
#     parent_phone = models.CharField(max_length=100)
#     classs = models.CharField(max_length=2, choices=CLASS_CHOICES)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#         if self.classs == 'j1':
#             Jss1.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 schoolNo=self.schoolNo,
#                 state=self.state,
#                 LGA=self.LGA,
#                 DOB=self.DOB,
#                 address=self.address,
#                 phone=self.phone,
#                 parent_phone=self.parent_phone,
#                 classs='Jss1',
#                 email=self.email,
#                 password=self.password
#             )
#         elif self.classs == 'j2':
#             Jss2.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 schoolNo=self.schoolNo,
#                 state=self.state,
#                 LGA=self.LGA,
#                 DOB=self.DOB,
#                 address=self.address,
#                 phone=self.phone,
#                 parent_phone=self.parent_phone,
#                 classs='Jss2',
#                 email=self.email,
#                 password=self.password
#             )
#         elif self.classs == 'j3':
#             Jss3.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 schoolNo=self.schoolNo,
#                 state=self.state,
#                 LGA=self.LGA,
#                 DOB=self.DOB,
#                 address=self.address,
#                 phone=self.phone,
#                 parent_phone=self.parent_phone,
#                 classs='Jss3',
#                 email=self.email,
#                 password=self.password
#             )
#         elif self.classs == 's1':
#             Ss1.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 schoolNo=self.schoolNo,
#                 state=self.state,
#                 LGA=self.LGA,
#                 DOB=self.DOB,
#                 address=self.address,
#                 phone=self.phone,
#                 parent_phone=self.parent_phone,
#                 classs='Ss1',
#                 email=self.email,
#                 password=self.password
#             )
#         elif self.classs == 's2':
#             Ss2.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 schoolNo=self.schoolNo,
#                 state=self.state,
#                 LGA=self.LGA,
#                 DOB=self.DOB,
#                 address=self.address,
#                 phone=self.phone,
#                 parent_phone=self.parent_phone,
#                 classs='Ss2',
#                 email=self.email,
#                 password=self.password
#             )
#         elif self.classs == 's3':
#             Ss3.objects.create(
#                 fullname=self.fullname,
#                 username=self.username,
#                 schoolNo=self.schoolNo,
#                 state=self.state,
#                 LGA=self.LGA,
#                 DOB=self.DOB,
#                 address=self.address,
#                 phone=self.phone,
#                 parent_phone=self.parent_phone,
#                 classs='Ss3',
#                 email=self.email,
#                 password=self.password
#             )

    
# class Enroll(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     phone = models.IntegerField()
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)
    

# class Adminn(AbstractUser):
#     user_permissions = models.ManyToManyField('auth.Permission', related_name='admin_user_permissions')
#     pass


# class Student(models.Model):
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     phone = models.IntegerField(max_length=25)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=150)


    

