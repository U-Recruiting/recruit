from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


# @login_required(login_url='/user/login')
def home(request, org_id):
    return render(request, 'resumes_view.html', context={'org_id': org_id})


# @login_required(login_url='/user/login')
def create_success(request):
    """
    新建职位成功
    ——————————
    :param request:
    :return:
    """
    return render(request, 'index06.html')


def create(request, org_id):
    return render(request, 'create_position.html', context={'org_id': org_id})


# @login_required(login_url='/user/login')
def positions(request):
    """
    已发布的职位
    ——————————
    :param request:
    :return:
    """
    return JsonResponse('')


def get_resume(request):
    """
    根据请求的项目返回对应的简历Json
    :param request:
    :return:
    """
    order = dict(request.POST)['resume_item']
    if order == 'received':
        return JsonResponse('')
    elif order == 'notified':
        return JsonResponse('')
    elif order == 'passed':
        return JsonResponse('')
    elif order == 'refused':
        return JsonResponse('')
    elif order == 'filtered':
        return JsonResponse('')


# 我收到的简历页面
def resume_view(request, org_id):
    return render(request, 'resumes_view.html', context={'org_id': org_id})


def position_view(request, org_id):
    return render(request, 'positions.html', context={'org_id': org_id})
