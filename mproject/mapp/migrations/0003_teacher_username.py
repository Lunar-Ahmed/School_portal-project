# Generated by Django 5.0.9 on 2024-11-27 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0002_alter_teacher_emergency_alter_teacher_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
