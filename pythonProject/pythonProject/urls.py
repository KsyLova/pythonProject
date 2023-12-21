"""
URL configuration for pythonProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy
from first_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', views.show_info),
    path('showWorker/<int:id_user>/', views.show_worker, name='show_worker'),
    path('showWorker/<int:id_user>/addsalary/', views.create_payout, name='create_payout'),
    path('showWorker/<int:id_user>/<str:number_pay>/<deletesalary/', views.delete_payout, name='delete_payout'),
    path('addSalary/', views.create_payout),
    path('', views.show_index, name='home'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('bossView/<int:id>/', views.show_department, name='show_department'),

    # ajax url
    path('ajax/validate_username', views.validate_username, name='validate_username'),
    path('ajax/validate_email', views.validate_email, name='validate_email'),
    path('ajax/check_numberPay', views.check_numberPay, name='check_numberPay')
]
