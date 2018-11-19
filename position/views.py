from django.shortcuts import render
from django.http import HttpResponse
from index.models import PositionInfo, PositionResumeStatus
from user.models import MyUser
import datetime
# Create your views here.


def details(request, position_id):
    buttin_text = '投递简历'
    user = request.user  # 可能为匿名用户

    if user.is_active:  # 如果不是匿名用户
        print(user.is_active)
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
            resume = user.resume_set.first()
            psr = PositionResumeStatus.objects.filter(position_id=position_id, resume_id=resume.id)
            if psr:
                disabled = "disabled"
                buttin_text = '已投递'
        else:
            logined = False
    else:
        logined = False

    position_info_detail = PositionInfo.objects.get(id=position_id)

    position_resumed = []
    resumed = position_info_detail.resume.all()
    for resume in resumed:
        # 每个简历对应的除了查询岗位信息的所以岗位信息
        positions = resume.positioninfo_set.exclude(id=position_info_detail.id)
        # 所以简历对应岗位信息汇总
        position_resumed += positions
    position_resumed = position_resumed[:2]


    post_time = position_info_detail.create_datetime

    now = datetime.datetime.now()
    timedelta = (now - post_time).days

    return render(request, 'jobinfo.html', locals())