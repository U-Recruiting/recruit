#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""


from django.urls import path
from . import views


urlpatterns = [
    path('<int:org_id>/', views.home),
    path('post/', views.post),
]
