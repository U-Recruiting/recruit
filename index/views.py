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

    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False
    return render(request, 'index.html', locals())





