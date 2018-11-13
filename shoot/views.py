from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from index.models import PositionInfo
# Create your views here.


# @login_required(login_url='/user/login')
def shoot(request, position_id):

    # 获取投递岗位
    position = PositionInfo.objects.get(id=position_id)

    # 该岗位那些人投递了

    position_resumed = []

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
    resume = request.user.resume_set.first()


    # 填入岗位信息表（多对多）
    position.resume.add(resume)

    return render(request, 'success.html', locals())
