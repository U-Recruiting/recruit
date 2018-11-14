#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""


from django.urls import path
from .views import home
from . import views

urlpatterns = [
    path('<int:org_id>/', home),
    path('register01/',views.register01),
    path('register02/',views.register02),
    path('myhome/',views.myhome),
    path('home01/',views.home01),
    path('post/', views.post)
]
