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
    # path('reset/',views.reset,name='reset'),
    # path('email_verify/',views.email_verify,name='email_verify'),



    path('test', views.test, name='test')
]