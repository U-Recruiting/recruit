#!usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:shenchen
@file: urls
@time: 2018/11/11
"""

from django.urls import path
from .views import home, create_success, positions, received_resumes, filtered_resumes, \
    refused_resumes, resume_view, position_view

urlpatterns = [
    path('<int:org_id>/', home),
    path('create/', create_success),
    path('positions/', position_view),
    path('received_resumes/<int:org_id>/', received_resumes),
    path('filtered_resumes/<int:org_id>/', filtered_resumes),
    path('refused_resumes/<int:org_id>', refused_resumes),
    path('resumes/', resume_view)
]
