# Generated by Django 4.2.6 on 2023-10-20 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_remove_worker_id_user_worker_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='worker',
            old_name='department',
            new_name='departments',
        ),
    ]
