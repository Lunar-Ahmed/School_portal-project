# Generated by Django 5.0.9 on 2024-12-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0012_remove_teacher_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Jss1',
        ),
        migrations.DeleteModel(
            name='Jss2',
        ),
        migrations.DeleteModel(
            name='Jss3',
        ),
        migrations.DeleteModel(
            name='Ss1',
        ),
        migrations.DeleteModel(
            name='Ss2',
        ),
        migrations.DeleteModel(
            name='Ss3',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Admission_Number',
            new_name='admission_number',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='DOB',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Gender',
            new_name='gender',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Middlename',
            new_name='middlename',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Password',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='Profile_Picture',
            new_name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Class',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Mobile',
        ),
        migrations.RemoveField(
            model_name='student',
            name='Parent_Mobile',
        ),
        migrations.AddField(
            model_name='student',
            name='class_level',
            field=models.CharField(choices=[('J1', 'JSS1'), ('J2', 'JSS2'), ('J3', 'JSS3'), ('S1', 'SS1'), ('S2', 'SS2'), ('S3', 'SS3')], max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_mobile',
            field=models.CharField(max_length=15, null=True),
        ),
    ]