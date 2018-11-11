#!/usr/bin/python3
# -*- coding:utf-8 -*-
# time    : 2018/11/8 10:49 AM
# author  : shenchen

from django.urls import path
from . import views

urlpatterns = [
    # path('login', views.loginView, name='login'),
    #ada添加
    path('login/', views.loginView, name='login'),

    path('register', views.registerView, name='register'),
    path('setpassword', views.setpasswordView, name='setpassword'),
    path('logout', views.logoutView, name='logout'),
    path('index', views.index, name='index'),
]