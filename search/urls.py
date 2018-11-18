#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/12
"""

from django.urls import path
from . import views

urlpatterns = [
    path('<int:page>', views.searchView, name='search'),
    path('searchmore', views.searchmoreView, name='searchmore'),
    path('company',views.companyView,name = 'company'),
    path('jobinfo',views.jobinfoView,name = 'jobinfo')
]

