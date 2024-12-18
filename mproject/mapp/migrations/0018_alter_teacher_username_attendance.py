# Generated by Django 5.0.9 on 2024-12-11 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0017_remove_teacher_is_disabled_alter_teacher_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='username',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField()),
                ('present_1', models.BooleanField(default=False)),
                ('present_2', models.BooleanField(default=False)),
                ('present_3', models.BooleanField(default=False)),
                ('present_4', models.BooleanField(default=False)),
                ('present_5', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mapp.student')),
            ],
        ),
    ]
