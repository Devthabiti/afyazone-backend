# Generated by Django 5.0.7 on 2024-08-06 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_rename_experiance_doctorprofile_experience_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewrating',
            options={'ordering': ['created']},
        ),
    ]
