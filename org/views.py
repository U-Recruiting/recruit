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


@login_required(login_url='/user/login')


def home(request):
    # user = MyUser.objects.get(email='120557727@qq.com')
    # orginfo = user.orginfo_set.all().first()
    # positions = orginfo.positioninfo_set.all()
    # received = utls.get_resume_item(positions, 'received')
    # print(received)
    return render(request, 'org_view.html', locals())


# def create(request):
#     user = request.user
#     orginfo = user.orginfo_set.all().first()
#     if request.method == 'POST':
#         type = request.POST.get('type', '')
#         name = request.POST.get('name', '')
#         department = request.POST.get('department', '')
#         job_catagory = request.POST.get('job_catagory', '')
#         start_salary = request.POST.get('start_salary', '')
#         end_salary = request.POST.get('end_salary', '')
#         city = request.POST.get('city', '')
#
#         distinct = request.POST.get('distinct', '')
#
#         address = request.POST.get('address', '')
#         work_exp = request.POST.get('work_exp', '')
#         edu_exp = request.POST.get('edu_exp', '')
#
#         tags = request.POST.get('tags', '')
#
#         desc = request.POST.get('desc', '')
#
#         positionAdvantage = request.POST.get('positionAdvantage', '')
#         subwayline = request.POST.get('subwayline', '')
#         linestaion = request.POST.get('linestaion', '')
#         create_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
#         position = PositionInfo(type=type, name=name, department=department, job_catagory=job_catagory,
#                                 start_salary=start_salary,
#                                 end_salary=end_salary, city=city, distinct=distinct, address=address,
#                                 work_exp=work_exp, edu_exp=edu_exp, tags=tags, desc=desc,
#                                 positionAdvantage=positionAdvantage, subwayline=subwayline, linestaion=linestaion,
#                                 create_datetime=create_datetime, org_id=orginfo.id)
#         position.save()
#         print('success')
#         return create_success(request)
#
#     return render(request, 'create_position.html', locals())


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
    positions = orginfo.positioninfo_set.all()

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
        return JsonResponse(json_positions, content_type="application/json,charset=utf-8")


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
                                                  interview_address=interview_address,
                                                  interview_datatime=interview_datatime,
                                                  status=status)

    return HttpResponse('get method')


def get_resume(request):
    """
    根据请求的项目返回对应的简历Json
    :param request:
    :return:
    """
    demo_json = [{"sex": "男",
                  "education": "硕士",
                  "email": "test@123.com",
                  "resume_id": 1,
                  "address": "亦庄文化园",
                  "name": "冰激淋",
                  "school": "联通学院",
                  "city": "北京",
                  "position_name": "java开发",
                  "position_id": 5312625,
                  "mobile": "18812312345",
                  "org": "中国联通",
                  "work_years": "1"},
                 {"sex": "女",
                  "education": "硕士",
                  "email": "test@123.com",
                  "resume_id": 1,
                  "address": "亦庄文化园",
                  "name": "大王卡",
                  "school": "联通学院",
                  "city": "北京",
                  "org": "中国移动",
                  "position_name": "java开发",
                  "position_id": 5312625,
                  "mobile": "18812312345",
                  "work_years": "1"}]
    order = dict(request.POST)['item'][0]
    if order == 'received':
        demo_json[0]['name'] = '你收到我的简历啦！'
        demo_json[1]['name'] = '你收到我的简历啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'notified':
        demo_json[0]['name'] = '我要找你面试啦！'
        demo_json[1]['name'] = '我要找你面试啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'passed':
        demo_json[0]['name'] = '我要入职啦！'
        demo_json[1]['name'] = '我也要入职啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'refused':
        demo_json[0]['name'] = '你拒绝了我！'
        demo_json[1]['name'] = '我也被你拒绝啦！'
        return JsonResponse(demo_json, safe=False)
    elif order == 'filtered':
        return JsonResponse(demo_json, safe=False)


def get_position(request):
    position_demo = [{
        "position_id": "10086",
        "position_name": "Python开发",
        "city": "北京",
        "position_type": "全栈、爬虫、数据分析",
        "min_salary": "8k",
        "max_salary": "10k",
        "work_exp": "1-3年",
        "edu_exp": "本科及以上",
        "post_date": "2018-11-18 14:44:44"
    },
        {
            "position_id": "10086",
            "position_name": "Java开发",
            "city": "北京",
            "position_type": "全栈、爬虫、数据分析",
            "min_salary": "8k",
            "max_salary": "10k",
            "work_exp": "1-3年",
            "edu_exp": "本科及以上",
            "post_date": "2018-11-18 14:44:44"
        }
    ]
    order = dict(request.POST)['item'][0]
    if order == 'valid':
        position_demo[0]['position_name'] = '我是有效职位！'
        position_demo[1]['position_name'] = '我也是有效职位！'
        return JsonResponse(position_demo, safe=False)
    elif order == 'invalid':
        position_demo[0]['position_name'] = 'Oh！我下线了~~！'
        position_demo[1]['position_name'] = '~~！'
        return JsonResponse(position_demo, safe=False)


def get_html(request):
    """
    根据请求返回对应的部分页面
    :param request:
    :return:
    """
    order = dict(request.POST)['html']
    print(type(order), order)

    if 'received' in order:
        return render(request, 'resume_div/div_resume_received.html')
    elif 'notified' in order:
        return render(request, 'resume_div/div_resume_notified.html')
    elif 'passed' in order:
        return render(request, 'resume_div/div_resume_passed.html')
    elif 'refused' in order:
        return render(request, 'resume_div/div_resume_refused.html')
    elif 'filtered' in order:
        return render(request, 'resume_div/div_resume_filtered.html')
    elif 'div_resume' in order:
        return render(request, 'resume_div/div_resume_content.html')
    elif 'div_position' in order:
        return render(request, 'position_div/div_position_content.html')
    elif 'create' in order:
        return render(request, 'create_div/create.html')
    elif 'create_success' in order:
        return render(request, 'create_div/create_success.html')


def org_view(request, item):
    # print(item)
    if item in ['resumes', 'positions', 'create']:
        return render(request, 'org_view.html')
    else:
        return HttpResponse('404!!!')
