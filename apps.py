from django.apps import AppConfig
from flask import views
from django.urls import path
from . import views

class EmpAppConfig(AppConfig):
    name = 'Emp_app'


urlpatterns = [
    path('', views.home),
]