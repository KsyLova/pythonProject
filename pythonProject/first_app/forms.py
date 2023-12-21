from django import forms
from django.core.exceptions import ValidationError
from django.utils.datetime_safe import date
from first_app.models import Salary
from bootstrap_datepicker_plus.widgets import DatePickerInput

''' class SalaryForms(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ('number', 'payout', 'date_salary')'''


class SalaryForms(forms.Form):
    number = forms.CharField(help_text="Введите номер выплаты:")
    payout = forms.CharField(help_text="Внесите сумму выплаты:")
    date_salary = forms.DateField(help_text="Выберите дату зачисления выплаты:", widget=DatePickerInput())

    def clean_date_salary(self):
        date_local = self.cleaned_data['date_salary']
        print(date.today().day - date_local.day)
        payout = self.cleaned_data['payout']
        if date.today().day - date_local.day > 5000 and payout == 5000:
            raise ValidationError()
        return date_local
