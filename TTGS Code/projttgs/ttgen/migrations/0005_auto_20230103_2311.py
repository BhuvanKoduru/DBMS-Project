# Generated by Django 3.2 on 2023-01-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ttgen', '0004_auto_20230103_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='max_numb_students',
            field=models.IntegerField(default=60),
        ),
        migrations.AlterField(
            model_name='room',
            name='seating_capacity',
            field=models.IntegerField(default=60),
        ),
    ]