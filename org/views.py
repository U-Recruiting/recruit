from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from index.models import *
from user.models import MyUser
from django.core import serializers
import datetime
import json
from . import utls

# Create your views here.


def test(request):
    return render(request, 'create.html', locals())

# @login_required(login_url='/user/login')


def home(request):
    user = MyUser.objects.get(email='120557727@qq.com')
    orginfo = user.orginfo_set.all().first()
    positions = orginfo.positioninfo_set.all()
    received = utls.get_resume_item(positions, 'received')
    print(received)
    return render(request, 'resumes_view.html', locals())


def create(request):
    user = request.user
    orginfo = user.orginfo_set.all().first()
    if request.method == 'POST':
        type = request.POST.get('type', '')
        name = request.POST.get('name', '')
        department = request.POST.get('department', '')
        job_catagory =  request.POST.get('job_catagory', '')
        start_salary = request.POST.get('start_salary', '')
        end_salary = request.POST.get('end_salary', '')
        city = request.POST.get('city', '')

        distinct = request.POST.get('distinct', '')

        address = request.POST.get('address', '')
        work_exp = request.POST.get('work_exp', '')
        edu_exp = request.POST.get('edu_exp', '')

        tags = request.POST.get('tags', '')

        desc = request.POST.get('desc', '')

        positionAdvantage = request.POST.get('positionAdvantage', '')
        subwayline = request.POST.get('subwayline', '')
        linestaion = request.POST.get('linestaion', '')
        create_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        position = PositionInfo(type=type, name=name, department=department,job_catagory=job_catagory,start_salary=start_salary,
                     end_salary=end_salary, city=city, distinct=distinct, address=address,
                     work_exp=work_exp, edu_exp=edu_exp, tags=tags, desc=desc,
                     positionAdvantage=positionAdvantage, subwayline=subwayline, linestaion=linestaion,
                     create_datetime=create_datetime, org_id=orginfo.id)
        position.save()
        print('success')
        return create_success(request)

    return render(request, 'create_position.html', locals())

# @login_required(login_url='/user/login')
def create_success(request):
    """
    新建职位成功
    ——————————
    :param request:
    :return:
    """
    return render(request, 'success.html')


def get_ajax_resumes(request):
    """
    根据请求的项目返回对应的简历Json
    :param request:
    :return:
    """
    # user = request.user
    user = MyUser.objects.get(email='120557727@qq.com')
    print(user.date_joined)
    orginfo = user.orginfo_set.all().first()
    positions= orginfo.positioninfo_set.all()

    if request.method == 'POST':
        order = request.POST.get('resume_item')
        received = utls.get_resume_item(positions, order)
        return HttpResponse(json.dumps(received, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return HttpResponse('test')

# @login_required(login_url='/user/login')


def get_ajax_positions(request):
    """
    已发布的职位
    ——————————
    :param request:
    :return:
    """
    user = MyUser.objects.get(email='120557727@qq.com')
    orginfo = user.orginfo_set.all().first()
    if request.method == 'POST':
        status = request.POST.get('status', '')
        positions = orginfo.positioninfo_set.filter(status=status)
        json_positions = serializers.serialize('json', positions)
    return HttpResponse(json_positions, content_type="application/json,charset=utf-8")


def positions(request):
    user = MyUser.objects.get(email='120557727@qq.com')
    orginfo = user.orginfo_set.all().first()
    positions = orginfo.positioninfo_set.filter(status='on')
    print(positions)
    return render(request, 'positions.html', locals())


def interview_or_pass_or_refuse_ajax(request):
    if request.method == 'POST':
        status = request.POST.get('status', '')
        position_id = int(request.POST.get('position_id', ''))
        resume_id = int(request.POST.get('resume_id', ''))
        interview_address = request.POST.get('interview_address', '')
        interview_datatime = request.POST.get('interview_datatime', '')

        return utls.update_pisition_resume_status(position_id=position_id, resume_id=resume_id,
                                           interview_address=interview_address, interview_datatime=interview_datatime,
                                           status=status)


    return HttpResponse('get method')


