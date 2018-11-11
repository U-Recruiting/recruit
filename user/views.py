from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.mail import send_mail
from django.conf import settings
import random
from .models import MyUser
from django.contrib.auth import login, logout, authenticate


# Create your views here.


@login_required(login_url='/user/login')
def index(request):
    return HttpResponse('test page')


# 用户登录
def loginView(request):
    remembered_email = request.COOKIES.get('remember_email', '')
    if remembered_email:
        checked = 'checked'
    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        remerber = request.POST.get('autoLogin',None)
        if MyUser.objects.filter(Q(mobile=email) | Q(email=email)):
            user = MyUser.objects.filter(Q(mobile=email) | Q(email=email)).first()
            if check_password(password, user.password):
                login(request, user)
                if user.role.name == 'org':
                    url = '/org/'+str(user.id)
                elif user.role.name == 'user':
                    url = '/'
                r = redirect(url)  ##应聘者进入index, 招聘者进入org/position
                if remerber:
                    r.set_cookie('remember_email', email)
                else:
                    r.delete_cookie('remember_email')
                    request.session.set_expiry(0)
                return r
            else:
                tips = '密码错误，请重新输入！'
        else:

                tips = '用户不存在'
    return render(request, 'login.html', locals())



# 用户注册
def registerView(request):
    title = '注册'
    button = '获取验证码'
    unit_1 = '/user/login'
    unit_1_name = '立即登录'
    unit_2 = '/user/setpassword'
    unit_2_name = '修改密码'

    if request.method == 'POST':
        email = request.POST.get('email', '')
        verification_code = request.POST.get('verificationCode', '')
        if MyUser.objects.filter(email=email):
            tips = '用户已存在'
        else:
            if not request.session.get('verification_code', ''):
                button = '用户注册'
                tips = '验证码已发送'
                verification_code = str(random.randint(100000, 999999))
                request.session['verification_code'] = verification_code
                from_email = settings.DEFAULT_FROM_EMAIL
                send_mail('用户注册', verification_code, from_email, [email])
            elif verification_code == request.session.get('verification_code'):
                user = MyUser.objects.create_user(username=email, email=email, password=verification_code, is_active=0)
                user.save()
                return redirect('test')
            else:
                tips = '验证码错误, 请重新获取'
                del request.session['verification_code']
    return render(request, 'register01.html', locals())


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
    return render(request, 'register.html', locals())


# 使用make_password实现密码修改
from django.contrib.auth.hashers import make_password


def setpasswordView_1(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        old_password = request.POST.get('password', '')
        new_password = request.POST.get('new_password', '')
        # 判断用户是否存在
        user = MyUser.objects.filter(username=username)
        if MyUser.objects.filter(username=username):
            user = authenticate(username=username, password=old_password)
            # 密码加密处理并保存到数据库
            dj_ps = make_password(new_password, None, 'pbkdf2_sha256')
            user.password = dj_ps
            user.save()
    return render(request, 'user', locals())


# 用户注销，退出登录
def logoutView(request):
    logout(request)
    return redirect('/')
