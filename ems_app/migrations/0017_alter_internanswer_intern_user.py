# Generated by Django 5.0.2 on 2024-02-22 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0016_alter_internanswer_intern_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internanswer',
            name='intern_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern_answer', to='ems_app.internuser'),
        ),
    ]