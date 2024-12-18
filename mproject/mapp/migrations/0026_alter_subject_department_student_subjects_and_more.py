# Generated by Django 5.0.9 on 2024-12-17 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0025_alter_department_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_department', to='mapp.student'),
        ),
        migrations.AddField(
            model_name='student',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
        migrations.AlterField(
            model_name='jss1',
            name='class_level',
            field=models.CharField(default='JSS1', max_length=5),
        ),
        migrations.AlterField(
            model_name='jss1',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jss2',
            name='class_level',
            field=models.CharField(default='JSS2', max_length=5),
        ),
        migrations.AlterField(
            model_name='jss2',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jss3',
            name='class_level',
            field=models.CharField(default='JSS3', max_length=5),
        ),
        migrations.AlterField(
            model_name='jss3',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ss1',
            name='class_level',
            field=models.CharField(default='SS1', max_length=5),
        ),
        migrations.AlterField(
            model_name='ss1',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ss2',
            name='class_level',
            field=models.CharField(default='SS2', max_length=5),
        ),
        migrations.AlterField(
            model_name='ss2',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='ss3',
            name='class_level',
            field=models.CharField(default='SS3', max_length=5),
        ),
        migrations.AlterField(
            model_name='ss3',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='admission_number',
            field=models.CharField(blank=True, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=250, unique=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=150),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
    ]
