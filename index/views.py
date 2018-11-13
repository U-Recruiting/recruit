from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Job_Label1,Dynamic_Position,Dynamic_Org,PositionInfo
# Create your views here.
#
# from docx import Document

# @login_required(login_url='/user/login')
def index(request):

    #标签1，2，3
    lables = Job_Label1.objects.all()
    lables_4 =[]
    for index in range(4):
         lables_4.append(lables[index])
    hot_position = Dynamic_Position.objects.select_related('position_info').order_by('-dynamic_search').all()[:10]
    print("hot_position:",hot_position)
    hot_company = Dynamic_Org.objects.select_related('org_info').order_by('-dynamic_search').all()[:10]
    print("hot_position:", hot_company)
    latest = PositionInfo.objects.order_by('-create_datetime').all()[:10]
    print("latest:",latest)
    return render(request, 'index.html', locals())

from index.models import *
def insert_label(request):
    a = '矿产 能源 环保'
    for i in a.split(' '):
        j = Job_Label3(name=i, parent_id=38)
        j.save()

    return HttpResponse('success')



