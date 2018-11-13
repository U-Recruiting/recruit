from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from index.models import PositionInfo
# Create your views here.


# @login_required(login_url='/user/login')
def shoot(request, position_id):

    # 获取投递岗位
    position = PositionInfo.objects.get(id=position_id)
    # 当前用户
    user = request.user

    # 获取用户简历
    resume = request.user.resume_set.first()

    # 填入岗位信息表（多对多）
    position.resume.add(resume)

    return HttpResponse(' %s %s' %(position.name, resume.id))
