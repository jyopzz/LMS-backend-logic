# Generated by Django 5.0.2 on 2024-02-15 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0004_alter_employeeuser_emailid_alter_internuser_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeuser',
            name='emailid',
        ),
        migrations.RemoveField(
            model_name='internuser',
            name='emailid',
        ),
    ]
