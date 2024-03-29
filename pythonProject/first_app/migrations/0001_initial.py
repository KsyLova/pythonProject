# Generated by Django 4.2.5 on 2023-09-21 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя:', max_length=150, verbose_name='Имя руководителя')),
                ('last_name', models.CharField(help_text='Введите фамилию:', max_length=150, verbose_name='Фамилия руководителя')),
            ],
            options={
                'db_table': ' Boss',
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_contract', models.CharField(help_text='Введите номер договора:', max_length=10, verbose_name='Номер договора')),
            ],
            options={
                'db_table': ' Contract',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название отдела:', max_length=150, verbose_name='Название отдела')),
                ('job_title', models.TextField(verbose_name='Полное название занимаемоемой должности')),
            ],
            options={
                'db_table': ' Department',
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя:', max_length=150, verbose_name='Имя сотрудника')),
                ('last_name', models.CharField(help_text='Введите фамилию:', max_length=150, verbose_name='Фамилия сотрудника')),
                ('date_work', models.DateField(help_text='Введите дату подписания трудового договора:', verbose_name='date')),
                ('contract', models.ForeignKey(help_text='Выберите договор:', on_delete=django.db.models.deletion.CASCADE, to='first_app.contract', verbose_name='name contract')),
            ],
            options={
                'db_table': ' Worker',
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payout', models.CharField(help_text='Внесите начальную ставку:', max_length=8, verbose_name='salary')),
                ('date_salary', models.DateField(help_text='Введите дату зачисления заработной платы:', verbose_name='Дата начисления заработной платы')),
                ('boss', models.ForeignKey(help_text='Выберите руководителя :', on_delete=django.db.models.deletion.CASCADE, to='first_app.boss', verbose_name='name')),
                ('worker', models.ForeignKey(help_text='Выберите сотрудника:', on_delete=django.db.models.deletion.CASCADE, to='first_app.worker', verbose_name='Сотрудник')),
            ],
            options={
                'db_table': ' Salary',
            },
        ),
        migrations.AddField(
            model_name='boss',
            name='departments',
            field=models.ForeignKey(help_text='Выберите название отдела:', on_delete=django.db.models.deletion.CASCADE, to='first_app.department', verbose_name='Название отдела'),
        ),
    ]
