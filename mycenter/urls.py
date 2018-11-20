#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/13
"""

from django.urls import path
from . import views

urlpatterns = [
    path('delivery', views.delivery, name='delivery'),
    path('mycollection', views.mycollection, name='mycollection'),
    path('collect/' ,views.collect, name ='collect'),
    path('companydetail/' ,views.companydetail,name = 'companydetail')

]
