"""Defines URL pattern for mypett"""
from django.urls import path
from . import views

app_name = "mypett"
urlpetterns = [
    # Homepage
    path('',views.index,name='index'),
]