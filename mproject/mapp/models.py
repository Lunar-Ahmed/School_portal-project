from django.db import models
# from django.contrib.auth.models import AbstractUser

class Enroll(models.Model):
    student_name = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=50)
    email = models.IntegerField()
    address = models.EmailField(max_length=100)
    Message = models.TextField(max_length=150)
    
    
class Teacher(models.Model):
    Passport = models.ImageField(upload_to='Profile/')
    Firstname = models.CharField(max_length=150, null=True)
    Middlename = models.CharField(max_length=150, null=True)
    Lastname = models.CharField(max_length=150, null=True)
    Mobile = models.IntegerField(max_length=150, null=True)
    Address = models.CharField(max_length=150, null=True)
    Sex = models.CharField(max_length=150, null=True)
    Emergency = models.IntegerField(max_length=150, null=True)
    Class =  models.CharField(max_length=150, null=True)
    Subject = models.CharField(max_length=150, null=True)
    DOB= models.DateTimeField()
    Cv = models.FileField()
    Email = models.EmailField(max_length=100)
    Password = models.CharField(max_length=150) 
       
# class Student(models.Model):
#     Profile = models.ImageField(upload_to='Profile/')
#     Firstname = models.CharField(max_length=150, null=True)
#     Middlename = models.CharField(max_length=150, null=True)
#     Lastname = models.CharField(max_length=150, null=True)
#     Mobile = models.IntegerField(max_length=150, null=True)
#     Address = models.CharField(max_length=150, null=True)
#     Sex = models.CharField(max_length=150, null=True)
#     Emergency = models.IntegerField(max_length=150, null=True)
#     Class =  models.CharField(max_length=150, null=True)
#     Subject = models.CharField(max_length=150, null=True)
#     DOB= models.DateTimeField()
#     Cv = models.FileField()
#     Email = models.EmailField(max_length=100)
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

class Jss1(models.Model):
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

class Jss2(models.Model):
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

class Jss3(models.Model):
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

class Ss1(models.Model):
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

class Ss2(models.Model):
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

class Ss3(models.Model):
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=40)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

class Student(models.Model):
    CLASS_CHOICES = [
        ('j1', 'Jss1'),  
        ('j2', 'Jss2'),
        ('j3', 'Jss3'),
        ('s1', 'Ss1'),
        ('s2', 'Ss2'),
        ('s3', 'Ss3'),
    ]
    fullname = models.CharField(max_length=350)
    username = models.CharField(max_length=100)
    schoolNo = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    LGA = models.CharField(max_length=100)
    DOB = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.BigIntegerField()
    parent_phone = models.CharField(max_length=100)
    classs = models.CharField(max_length=2, choices=CLASS_CHOICES)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.classs == 'j1':
            Jss1.objects.create(
                fullname=self.fullname,
                username=self.username,
                schoolNo=self.schoolNo,
                state=self.state,
                LGA=self.LGA,
                DOB=self.DOB,
                address=self.address,
                phone=self.phone,
                parent_phone=self.parent_phone,
                classs='Jss1',
                email=self.email,
                password=self.password
            )
        elif self.classs == 'j2':
            Jss2.objects.create(
                fullname=self.fullname,
                username=self.username,
                schoolNo=self.schoolNo,
                state=self.state,
                LGA=self.LGA,
                DOB=self.DOB,
                address=self.address,
                phone=self.phone,
                parent_phone=self.parent_phone,
                classs='Jss2',
                email=self.email,
                password=self.password
            )
        elif self.classs == 'j3':
            Jss3.objects.create(
                fullname=self.fullname,
                username=self.username,
                schoolNo=self.schoolNo,
                state=self.state,
                LGA=self.LGA,
                DOB=self.DOB,
                address=self.address,
                phone=self.phone,
                parent_phone=self.parent_phone,
                classs='Jss3',
                email=self.email,
                password=self.password
            )
        elif self.classs == 's1':
            Ss1.objects.create(
                fullname=self.fullname,
                username=self.username,
                schoolNo=self.schoolNo,
                state=self.state,
                LGA=self.LGA,
                DOB=self.DOB,
                address=self.address,
                phone=self.phone,
                parent_phone=self.parent_phone,
                classs='Ss1',
                email=self.email,
                password=self.password
            )
        elif self.classs == 's2':
            Ss2.objects.create(
                fullname=self.fullname,
                username=self.username,
                schoolNo=self.schoolNo,
                state=self.state,
                LGA=self.LGA,
                DOB=self.DOB,
                address=self.address,
                phone=self.phone,
                parent_phone=self.parent_phone,
                classs='Ss2',
                email=self.email,
                password=self.password
            )
        elif self.classs == 's3':
            Ss3.objects.create(
                fullname=self.fullname,
                username=self.username,
                schoolNo=self.schoolNo,
                state=self.state,
                LGA=self.LGA,
                DOB=self.DOB,
                address=self.address,
                phone=self.phone,
                parent_phone=self.parent_phone,
                classs='Ss3',
                email=self.email,
                password=self.password
            )

    
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


    

