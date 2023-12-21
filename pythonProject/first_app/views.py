import hashlib

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from first_app.models import Worker, Salary, Boss, Department
from first_app.forms import SalaryForms


def show_info(request):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name="Начальники").exists():
            boss = Boss.objects.get(id_user_id=user.id)
            departments = list(Department.objects.filter(boss=boss.id))
            return render(request, 'bossView.html', {"departments": departments})
        else:
            worker = Worker.objects.get(id_user_id=user.id)
            salary = Salary.objects.filter(worker=worker.id)
            salary = list(salary)
            return render(request, 'workerinfo.html',
                          {"worker": worker, "link_img": hashlib.md5(user.email.encode('utf-8')).hexdigest(),
                           "salary": salary, "request": 0})
    else:
        return redirect("")


def show_worker(request, id_user):
    user = request.user
    if user.is_authenticated and user.groups.filter(name="Начальники").exists():
        worker = Worker.objects.get(id_user_id=id_user)
        salary = Salary.objects.filter(worker=worker.id)
        salary = list(salary)
        return render(request, 'workerinfo.html',
                      {"worker": worker, "link_img": hashlib.md5(User.objects.get(id=worker.id_user_id).email.encode('utf-8')).hexdigest(),
                       "salary": salary, "request": 1})
    else:
        return render(request, 'notAccess.html')


def show_index(request):
    if request.method == "GET":
        cur_user = request.user
        if cur_user.is_authenticated:
            return redirect("/info")
        else:
            return render(request, 'index.html')
    else:
        print(request.body)
        if (request.POST.get("email") != None):
            email = request.POST.get("email")
            password = request.POST.get("password")
            username = User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
            try:
                login(request, user)
                return redirect("/info")
            except Exception:
                print("Неверный email или пароль")
                return redirect("/")
        else:
            email = request.POST.get("create_email")
            username = request.POST.get("create_user_name")
            password = request.POST.get("create_password")
            user = User.objects.create_user(email=email, username=username, password=password)
            login(request, user)
            return redirect("/info")


def create_payout(request, id_user):
    if request.method == "GET":
        form = SalaryForms()
        return render(request, 'templateForm.html', {"form": SalaryForms})
    else:
        form = SalaryForms(request.POST)
        worker = Worker.objects.get(id_user_id=id_user)
        if form.is_valid():
            obj = Salary.objects.create(
                worker_id=Worker.objects.get(id_user_id=id_user).id,
                boss_id=Boss.objects.get(departments=worker.departments).id,
                number=form.cleaned_data['number'],
                payout=form.cleaned_data['payout'],
                date_salary=form.cleaned_data['date_salary']
            )
            '''salary = form.save(commit=False)
            salary.worker = Worker.objects.get(id_user_id=id_user)
            salary.boss = Boss.objects.get(departments=salary.worker.departments)
            salary.save()'''
            return redirect("/info")
        else:
            return redirect("/")


def delete_payout(request, id_user, number_pay):
    worker_id = Worker.objects.get(id_user_id=id_user).id
    pay = Salary.objects.filter(number=number_pay, worker_id=worker_id).first().delete()
    return redirect("/info")


def show_department(request, id):
    departments = Department.objects.get(id=id)
    worker = list(Worker.objects.filter(departments=departments.id))
    return render(request, 'bossViewDepartments.html', {"workers": worker})


# AJAX views

def validate_username(request):
    username = request.GET.get('create_user_name', None)
    print(username)
    response = {
        'taken': User.objects.filter(username__exact=username).exists()
    }
    return JsonResponse(response)


def validate_email(request):
    email = request.GET.get('create_email', None)
    response = {
        'taken': User.objects.filter(email__exact=email).exists()
    }
    return JsonResponse(response)


def check_numberPay(request):
    number = request.GET.get('number', None)
    response = {
        'taken': Salary.objects.filter(number__exact=number).exists()
    }
    return JsonResponse(response)
# Create your views here.
