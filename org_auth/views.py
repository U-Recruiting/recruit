from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
import datetime
from PIL import Image
from index.models import PositionInfo, OrgInfo
import os

# Create your views here.


@login_required(login_url='/user/login')
def home(request):
    return HttpResponse('hello')


def register01(request):
    user = request.user
    if request.method == "GET":
        return render(request,"register01.html")
    if request.method == 'POST':
        main_page = request.POST.get('main_page', '')
        company_name = request.POST.get('company_name', '')
        company_license = request.FILES.get('company_license', '')
        print(main_page,company_name,company_license)
        # orginfo = OrgInfo(url=main_page, name=company_name, user_id=user.id)
        # orginfo.save()
        # licese_path = os.path.join(settings.BASE_DIR, 'org_auth/static/license/' + str(orginfo.id)+'.jpg')
        # Image.open(company_license).save(licese_path)
        # OrgInfo.objects.filter(user_id=user.id).update(lincese = licese_path)
        return redirect('/org_auth/register02')
    return HttpResponse('success')


def register02(request):
    return render(request, 'register02.html')


def conplete_orginfo(request):
    user = request.user
    if request.method == "GET":
        return render(request,"home.html")
    if request.method == 'POST':
        company_name = request.POST.get('company_name', '')
        logo = request.FILES.get('logo', '')
        company_email = request.POST.get('company_email', '')
        city = request.POST.get('company_city', '')
        type = request.POST.get('select_industry_hidden', '')
        phase = request.POST.get('phse', '')
        scale = request.POST.get('select_scale_hidden', '')
        tages = request.POST.get('myfiles', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        createTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print([company_name,logo,company_email,city,type,phase,scale,tages,phone,desc])
        # orginfo = user.orginfo_set.all().first()
        # logo_path = os.path.join(settings.BASE_DIR, 'org_auth/static/logo'+orginfo.id+'.jpg')
        # OrgInfo.objects.filter(user_id=user.id).update(name=company_name, avatar=logo_path,
        #                                                type=type, phase=phase, desc=desc, scale=scale,
        #                                                phone=phone, city=city, company_email=company_email,
        #                                                tages=tages,createTime=createTime)
        return redirect('/org')
    return render(request, 'home.html', locals())

def home01(request):
    return render(request, 'home.html') ##完善公司信息

def myhome(request):
    return render(request,'myhome.html')