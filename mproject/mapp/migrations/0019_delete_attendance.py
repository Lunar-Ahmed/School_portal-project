# Generated by Django 5.0.9 on 2024-12-11 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0018_alter_teacher_username_attendance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]