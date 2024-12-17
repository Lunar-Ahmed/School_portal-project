# Generated by Django 5.0.9 on 2024-12-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapp', '0030_jss1_subjects_jss2_subjects_jss3_subjects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='Subject_Teacher',
            field=models.CharField(blank=True, choices=[('Mathematics', 'Mathematics(general)'), ('English', 'English(general)'), ('Civic Education', 'Civic Education(general)'), ('Biology', 'Biology(general)'), ('Chemistry', 'Chemistry(science)'), ('Physics', 'Physics(civic)'), ('Data Processing', 'Data-Processing(general)'), ('Marketing', 'Marketing(commercial)'), ('Economics', 'Economic(general)'), ('Computer Studies', 'Computer-Studies(general)'), ('Furthser Math', 'Further-Math(science)'), ('Government', 'Government(art, commercial)'), ('Literature', 'Literature(art)'), ('Commerce', 'Commerce(commercial)'), ('Accounting', 'Accounting(commercial)'), ('History', 'History(art)'), ('Geography', 'Geography(science)'), ('Book Keeping', 'Book-Keeping(science)'), ('Islamic Studies', 'Islamic-Studies(general)'), ('Christain Studies', 'Christain-Studies(general)'), ('Technical Drawing', 'Technical-Drawing(science)')], max_length=30, null=True),
        ),
    ]
