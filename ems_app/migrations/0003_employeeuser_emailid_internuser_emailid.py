# Generated by Django 5.0.2 on 2024-02-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0002_employeeuser_user_internuser_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeuser',
            name='emailid',
            field=models.CharField(default=1, max_length=250),
        ),
        migrations.AddField(
            model_name='internuser',
            name='emailid',
            field=models.CharField(default=1, max_length=250),
        ),
    ]
