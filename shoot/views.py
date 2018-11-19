from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from index.models import PositionInfo, PositionResumeStatus
from user.models import MyUser
# Create your views here.
import json

# @login_required

def shoot(request):
    position_id = request.POST.get('position_id', '')
    # # 获取投递岗位
    position = PositionInfo.objects.get(id=position_id)
    print(position_id)
    # 该岗位那些人投递了

    position_resumed = []
    #
    # 该岗位所以简历
    resumed = position.resume.all()
    for resume in resumed:
        # 每个简历对应的除了查询岗位信息的所以岗位信息
        positions = resume.positioninfo_set.exclude(id=position.id)
        # 所以简历对应岗位信息汇总
        position_resumed += positions
    # 当前用户
    user = request.user
    # 获取用户简历
    resume = user.resume_set.first()


    # 填入岗位信息表（多对多）
    position.resume.add(resume)

    prs = PositionResumeStatus.objects.filter(position_id=position.id, resume_id=resume.id)
    if not prs:
        PositionResumeStatus(position_id=position.id, resume_id=resume.id,status='received').save()
    if request.user.is_active:
        data = {"to": "success"}
    else:
        url = '/user/login/?next=/position/{0}'.format(position_id)
        data = {"to":url}
    return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")

