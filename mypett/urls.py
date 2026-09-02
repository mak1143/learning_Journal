"""Defines URL pattern for mypett"""
from django.urls import path
from . import views

app_name = "mypett"
urlpatterns = [
    # Homepage
    path('',views.index,name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topics, name='topics'),
]