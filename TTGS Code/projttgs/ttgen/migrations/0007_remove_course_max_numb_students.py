# Generated by Django 3.2 on 2023-01-04 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0006_meetingtime_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='max_numb_students',
        ),
    ]