# Generated by Django 5.0.9 on 2024-12-17 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0028_alter_student_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='department',
            field=models.CharField(choices=[('Science', 'Science'), ('Art', 'Art'), ('Commercial', 'Commercial')], max_length=15),
        ),
    ]