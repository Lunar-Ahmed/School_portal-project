# Generated by Django 5.0.9 on 2024-12-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0011_remove_jss1_lga_remove_jss1_address_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
    ]