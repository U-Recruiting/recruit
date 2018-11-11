#!usr/bin/python
#-*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""


from django.urls import path
from .views import home


urlpatterns = [
    path('<int:org_id>/', home),
]
