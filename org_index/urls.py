# -*- coding:utf-8 -*-


from django.urls import path
from . import views

urlpatterns = [
    path('<int:org_id>/', views.home),
    path('create/<int:org_id>/', views.create),
    path('positions/<int:ord_id>/', views.position_view),
    path('resumes/<int:org_id>/', views.resume_view),
    path('get_resumes/', views.get_resume, name='get_resumes')
]
