#!/usr/bin/python3
# -*- coding:utf-8 -*-
# time    : 2018/11/8 10:49 AM
# author  : shenchen

from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.registerView, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('setpassword/', views.setpasswordView, name='setpassword'),



    path('test', views.test, name='test')
]