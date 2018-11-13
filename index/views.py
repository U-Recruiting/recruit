from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Job_Label1,Dynamic_Position,Dynamic_Org,PositionInfo
# Create your views here.

# @login_required(login_url='/user/login')
def index(request):

    #标签1，2，3
    lables = Job_Label1.objects.all()
    print(lables)
    hot_position = Dynamic_Position.objects.select_related('position_info').order_by('-dynamic_search').all()[:10]

    hot_company = Dynamic_Org.objects.select_related('org_info').order_by('-dynamic_search').all()[:10]

    latest = PositionInfo.objects.order_by('-create_datetime').all()[:10]

    return render(request, 'index.html', locals())



