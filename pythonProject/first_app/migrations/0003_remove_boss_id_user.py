# Generated by Django 4.2.5 on 2023-10-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_boss_id_user_worker_id_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boss',
            name='id_user',
        ),
    ]