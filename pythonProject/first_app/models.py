from django.db import models
from django.contrib.auth.models import User


class IntegerRangeField(models.IntegerField):
    def __int__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(**kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Department(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="id отдела",
                              help_text="выберите отдел", null=False, blank=False)
    name = models.CharField(max_length=150, verbose_name="Название отдела",
                            help_text="Введите название отдела:", null=False, blank=False)
    job_title = models.TextField(verbose_name="Полное название занимаемоемой должности")


    def __str__(self):
        return "Отдел: " + self.name

    class Meta:
        db_table = " Department"


class Contract(models.Model):
    name_contract = models.CharField(max_length=10, verbose_name="Номер договора",
                                     help_text="Введите номер договора:", null=False, blank=False)

    # rate = IntegerRangeField(min_value=15000, max_value=60000, verbose_name="initial rate",
    # help_text="Введите начальную ставку:", null=False, blank=False)

    def __str__(self):
        return "Номер договора: " + self.name_contract

    class Meta:
        db_table = " Contract"


class Worker(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя сотрудника",
                                  help_text="Введите имя:", null=False, blank=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия сотрудника",
                                 help_text="Введите фамилию:", null=False, blank=False)
    date_work = models.DateField(verbose_name="date",
                                 help_text="Введите дату подписания трудового договора:", null=False, blank=False)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name="name contract",
                                 help_text="Выберите договор:", null=False, blank=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id пользователя",
                              help_text="выберите пользователя", null=True, blank=True)
    departments = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name="Название отдела",
                                    help_text="Выберите название отдела:", null=True, blank=False)


    def __str__(self):
        return "Сотрудник: " + self.first_name + " " + self.last_name + " " + self.contract.__str__()

    class Meta:
        db_table = " Worker"


class Boss(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="Имя руководителя",
                                  help_text="Введите имя:", null=False, blank=False)
    last_name = models.CharField(max_length=150, verbose_name="Фамилия руководителя",
                                 help_text="Введите фамилию:", null=False, blank=False)
    departments = models.ManyToManyField(Department)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="id пользователя",
                              help_text="выберите пользователя", null=True, blank=True)

    def __str__(self): return "Начальник: " + self.first_name + " " + self.last_name

    class Meta:
        db_table = " Boss"


class Salary(models.Model):
    number = models.CharField(max_length=8, verbose_name="Код выплаты",
                               help_text="Введите код выплаты:", null=False, blank=False)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Сотрудник",
                               help_text="Выберите сотрудника:", null=False, blank=False)
    boss = models.ForeignKey(Boss, on_delete=models.CASCADE, verbose_name="name",
                             help_text="Выберите руководителя :", null=False, blank=False)
    payout = models.CharField(max_length=8, verbose_name="Ставка",
                              help_text="Внесите начальную ставку:", null=False, blank=False)
    date_salary = models.DateField(verbose_name="Дата начисления заработной платы",
                                   help_text="Введите дату зачисления заработной платы:", null=False, blank=False)

    def __str__(self):
        return "Сотрудник " + self.worker.__str__() + " получил выплату " + self.date_salary.__str__() + " в размере " + self.payout

    class Meta:
        db_table = " Salary"
# Create your models here.
