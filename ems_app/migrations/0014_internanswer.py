# Generated by Django 5.0.2 on 2024-02-20 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0013_alter_employeeuser_user_alter_internuser_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('intern_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intern_answers', to='ems_app.internuser')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ems_app.module')),
            ],
        ),
    ]
