# Generated by Django 5.0.9 on 2024-12-17 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0029_alter_subject_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='jss1',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
        migrations.AddField(
            model_name='jss2',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
        migrations.AddField(
            model_name='jss3',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
        migrations.AddField(
            model_name='ss1',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
        migrations.AddField(
            model_name='ss2',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
        migrations.AddField(
            model_name='ss3',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='mapp.subject'),
        ),
    ]
