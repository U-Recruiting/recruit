from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


# @login_required(login_url='/user/login')
def home(request, org_id):
    return render(request, 'create.html', context={'org_id': org_id})


# @login_required(login_url='/user/login')
def create_success(request):
    """
    新建职位成功
    ——————————
    :param request:
    :return:
    """
    return render(request, 'index06.html')


# @login_required(login_url='/user/login')
def positions(request):
    """
    已发布的职位
    ——————————
    :param request:
    :return:
    """
    return JsonResponse('')


# @login_required(login_url='/user/login')
def received_resumes(request):
    """
    待处理/已收到的简历
    ——————————
    :param request:
    :return:
    """
    return JsonResponse('')


# @login_required(login_url='/user/login')
def filtered_resumes(request):
    """
    被自动过滤掉的简历
    ———————————————
    :param request:
    :return:
    """
    return JsonResponse('')


# @login_required(login_url='/user/login')
def refused_resumes(request):
    """
    不合适的简历
    ——————————
    :param request:
    :return:
    """
    return JsonResponse('')


# @login_required(login_url='/user/login')
def noticed_resumes(request):
    """
    已通知的简历
    ——————————
    :param request:
    :return:
    """
    return JsonResponse('')


# 简历页面，根据不同需求填充
def resume_view(request):
    return render(request, 'resumes_view.html')


def position_view(request):
    return render(request, 'positions.html')
