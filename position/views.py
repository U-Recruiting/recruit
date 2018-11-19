from django.shortcuts import render
from django.http import HttpResponse
from index.models import PositionInfo, PositionResumeStatus
from user.models import MyUser
# Create your views here.


def details(request, position_id):

    # user = MyUser.objects.get(email='ronnik@163.com')
    # resume = user.resume_set.first()
    # position_info_detail = PositionInfo.objects.get(id=position_id)
    #
    # is_shoot = False
    # psr = PositionResumeStatus.objects.filter(position_id=position_id, resume_id=resume.id)
    # if psr:
    #     is_shoot = True
    # print(is_shoot)
    return render(request, 'create.html', locals())