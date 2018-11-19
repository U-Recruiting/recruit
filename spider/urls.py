#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/17
"""
from django.urls import path
from . import views
urlpatterns = [
    path('start/', views.spider)
]
