from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import random
import json
import datetime
from .models import MyUser, Role
from django.contrib.auth import login, logout, authenticate
from PIL import Image
import os
import random
from . import utils
# Create your views here.

#用户密码重置
def reset(request):
    return render(request,'reset.html')
#邮箱验证
def email_verify(request):
    return render(request,'email_verify_test3.html')
#重置密码
def updatepwd(request):
    return render(request,'updatepwd.html')
#淘职用户协议
def privacy(request):
    return render(request,'privacy.html')

def test(request):
    index = chr(random.randint(97,106))
    path = os.path.join(settings.BASE_DIR, 'static/avatar/' + str(index)+'.jpg')
    user_path = os.path.join(settings.BASE_DIR, 'resume/static/avatar/'+str(1)+'.jpg')
    img = Image.open(path)
    img.save(user_path)
    return HttpResponse('test')



# 用户登录
def loginView(request):
    next = request.GET.get('next', '')
    if next:
        link = "/user/login/?next="+next
    else:
        link = "/user/login/"
    print(next)
    remembered_email = request.COOKIES.get('remember_email', '')
    if remembered_email:
        checked = 'checked'
    if request.method == 'POST':
        account = request.POST.get('account', '')
        password = request.POST.get('password', '')
        phone = request.POST.get('phone', '')
        code_password = request.POST.get('code_password', '')
        remerber = request.POST.get('autoLogin', None)
        if account:
            login_name = account
            login_password = password
        elif phone:
            login_name = phone
            login_password = code_password
        print(phone)
        if MyUser.objects.filter(Q(mobile=login_name) | Q(email=login_name)):
            user = MyUser.objects.filter(Q(mobile=login_name) | Q(email=login_name)).first()
            print(user)
            if check_password(login_password, user.code_password) or check_password(login_password, user.password):
            # if user:
                print('pass')
                login(request, user)
                if user.role.name == 'org':
                    if user.is_active == 1:
                        url = '/org/'
                    else:
                        url = '/org_auth/register01'
                elif user.role.name == 'user':
                    if next:
                        url = next
                    else:
                        if user.is_active:
                            url = '/'
                        else:
                            url = '/resume/myresume'
                    print(url)
                r = redirect(url)   ##应聘者进入index, 招聘者进入org/position
                if remembered_email:
                    if not remerber:
                        r.delete_cookie('remember_email')
                        request.session.set_expiry(0)
                else:
                    if remerber:
                        r.set_cookie('remember_email', account)
                return r
            else:
                tips = '密码错误，请重新输入！'
        else:
            tips = '用户不存在'
    return render(request, 'login.html', locals())


# 用户注册
def registerView(request):

    if request.method == 'POST':
        role_type = int(request.POST.get('type', ''))+1
        phone = request.POST.get('phone', '')
        verification_code = request.POST.get('verificationCode', '')
        if MyUser.objects.filter(email=phone): #测试
            tips = '用户已存在,请直接登录！'
        else:
            if verification_code == request.session.get('verification_code'):
                date_joined = datetime.datetime.now()
                role = Role.objects.get(id=role_type)
                user = MyUser.objects.create_user(username='', first_name='', last_name='', email=phone, password='',code_password='',
                                                  is_superuser=0,is_active=0, is_staff=0, date_joined=date_joined, mobile='', role_id=role.id)
                user.save()
                if user.role == 1:
                    return redirect('/resume/myresume')
                elif user.role == 2:
                    return redirect('/org_auth/register01')
            else:
                tips = '验证码错误, 请重新获取'
                del request.session['verification_code']
    return render(request, 'register.html', locals())


def get_verification_code(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', '')
        verification_code = str(random.randint(100000, 999999))
        request.session['verification_code'] = verification_code
        from_email = settings.DEFAULT_FROM_EMAIL
        send_mail('用户注册', verification_code, from_email, [phone]) # 先用email发送
        # text = '您的验证码是：'+verification_code+'。请不要把验证码泄露给其他人。'
        # resp = utils.send_sms(text=text, mobile=phone)
        # print(resp.decode('utf-8'))
        data = {'message': 'success'}
        return HttpResponse(json.dumps(data, ensure_ascii=False), content_type="application/json,charset=utf-8")
    return HttpResponse('get method')

# 修改密码
def setpasswordView(request):
    # 设置标题和另外两个URL链接
    title = '修改密码'
    unit_2 = '/user/login'
    unit_2_name = '立即登录'
    unit_1 = '/user/register'
    unit_1_name = '立即注册'
    new_password = True
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        if MyUser.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            user.set_password(new_password)
            user.save()
            tips = '密码修改成功'
        else:
            tips = '用户不存在'
    return render(request, 'test/register.html', locals())


# 使用make_password实现密码修改
from django.contrib.auth.hashers import make_password


def changepwd(request):

    user = request.user
    if request.method == 'POST':
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        old_password_sha = make_password(old_password, None, 'pbkdf2_sha256')
        if old_password_sha == user.password:
            new_password_sha = make_password(new_password, None, 'pbkdf2_sha256')
            user.password = new_password_sha
            user.save()
            tips = '修改密码成功'
        else:
            tips = '密码错误'

    return render(request, 'user.html', locals())


# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('/')
