from django.shortcuts import render
from django.http import HttpResponse
from index.models import *
# Create your views here.
import json

def delivery(request):

    # 当前用户
    # user = request.user
    #
    # print(user)
    #
    # # 当前用户简历
    # resume = user.resume_set.all()[0]
    #
    # # 简历所投岗位
    # positions = resume.positioninfo_set.all()
    #
    # print(positions)

    return render(request, 'deliverybox_test.html', locals())


def mycollection(request):
    user = request.user  # 可能为匿名用户

    if user.is_active:  # 如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False

    if request.method == 'GET':
        collections =Collection.objects.filter(user_id=user.id)
        positions = []
        for collection in collections:
            collection.position.adv = collection.position.positionAdvantage.split(',')[:2]
            positions.append(collection.position)
    return render(request, 'myjob_collection.html', locals())


def collect(request):
    print(request.POST)
    user = request.user
    if request.method == 'POST':
        print(request.POST)
        position_id = request.POST.get('position_id', '')
        Collection.objects.create(position_id=position_id, user_id=user.id)
        data = {"message": "success"}
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")

    return HttpResponse('ok')

def companydetail(request):
    return render(request, 'companydetail.html')