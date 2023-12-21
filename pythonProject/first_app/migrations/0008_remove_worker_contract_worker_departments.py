# Generated by Django 4.2.6 on 2023-10-20 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0007_remove_worker_departments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='contract',
        ),
        migrations.AddField(
            model_name='worker',
            name='departments',
            field=models.ForeignKey(help_text='Выберите название отдела:', null=True, on_delete=django.db.models.deletion.CASCADE, to='first_app.department', verbose_name='Название отдела'),
        ),
    ]
