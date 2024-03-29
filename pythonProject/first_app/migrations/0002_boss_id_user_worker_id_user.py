# Generated by Django 4.2.5 on 2023-10-03 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='id_user',
            field=models.ForeignKey(blank=True, help_text='выберите пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя'),
        ),
        migrations.AddField(
            model_name='worker',
            name='id_user',
            field=models.ForeignKey(blank=True, help_text='выберите пользователя', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id пользователя'),
        ),
    ]
