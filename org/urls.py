#!usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""

from django.urls import path
from . import views

app_name = 'org'
urlpatterns = [
    path('test/', views.test),

    # path('', views.home),  # home 默认显示待处理简历
    # path('create/', views.create),  # 发布职位
    # path('create_success/', views.create_success, name='create_success'),
    # path('get_ajax_resumes/', views.get_ajax_resumes, name='resumes'),

    # path('get_ajax_positions', views.get_ajax_positions, name='get_ajax_positions'),
    # path('positions/', views.positions, name='positions'),

    # path('interview_or_pass_or_refuse', views.interview_or_pass_or_refuse_ajax, name='interview_or_pass_or_refuse'),

    path('my_org/<str:item>/', views.org_view),
    path('get_resumes/', views.get_resume, name='get_resumes'),
    path('get_html/', views.get_html, name='get_html'),

]
