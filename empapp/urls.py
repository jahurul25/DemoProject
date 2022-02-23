from django.urls import path
from . import views

urlpatterns = [
    path('login', views.UserLogin.as_view(), name='UserLogin'), 
    path('employee', views.EmployeeInfo.as_view(), name='EmployeeInfo'), 
    path('employee/<int:id>', views.FindEmployeeInfo.as_view(), name='FindEmployeeInfo'), 

    path("employee-list", views.EmployeeList, name='EmployeeList')
]