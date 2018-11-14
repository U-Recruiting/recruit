from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required(login_url='/user/login')
def home(request, org_id):
    return HttpResponse('hello' + str(org_id))


def register01(request):

    return render(request, 'register01.html')


def register02(request):
    return render(request, 'register02.html')


def myhome(request):
    return render(request, 'myhome.html')


def home01(request):
    return render(request, 'home.html')


def post(request):
    return HttpResponse('skfjakfajk')