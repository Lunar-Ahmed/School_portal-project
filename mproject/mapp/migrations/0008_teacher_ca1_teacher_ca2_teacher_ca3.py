# Generated by Django 5.0.9 on 2024-12-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0007_studentscore_inputtable'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='ca1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='ca2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='teacher',
            name='ca3',
            field=models.IntegerField(default=0),
        ),
    ]