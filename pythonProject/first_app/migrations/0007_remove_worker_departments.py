# Generated by Django 4.2.6 on 2023-10-20 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0006_rename_department_worker_departments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='departments',
        ),
    ]
