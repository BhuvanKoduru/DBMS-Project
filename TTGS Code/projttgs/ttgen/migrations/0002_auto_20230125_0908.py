# Generated by Django 3.2 on 2023-01-25 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingtime',
            name='day',
            field=models.CharField(choices=[('MON', 'MON'), ('TUE', 'TUE'), ('WED', 'WED'), ('THR', 'THR'), ('FRI', 'FRI'), ('SAT', 'SAT')], max_length=15),
        ),
        migrations.AlterField(
            model_name='meetingtime',
            name='time',
            field=models.CharField(choices=[('7:30 - 8:30', '7:30 - 8:30'), ('8:30 - 9:30', '8:30 - 9:30'), ('9:30 - 10:30', '9:30 - 10:30'), ('11:00 - 11:50', '11:00 - 11:50'), ('11:50 - 12:40', '11:50 - 12:40'), ('12:40 - 1:30', '12:40 - 1:30'), ('2:30 - 3:30', '2:30 - 3:30'), ('3:30 - 4:30', '3:30 - 4:30'), ('4:30 - 5:30', '4:30 - 5:30')], default='11:30 - 12:30', max_length=50),
        ),
    ]
