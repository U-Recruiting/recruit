from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from index.models import *
from django.contrib.auth.decorators import login_required
from urllib.parse import unquote
import datetime

def searchView(request):
    #
    user = request.user  # 可能为匿名用户
    if user.is_active:  # 如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False
    #
    if request.method == 'GET':

        kword = request.session.get('search_input', '')
        print('keyword', kword)
        page = request.GET.get('pn', 1)
        city =request.GET.get('city', '')
        distinct =request.GET.get('distinct', '')
        work_exp =request.GET.get('workExpSelectInput', '')
        edu_exp =request.GET.get('eduExpSelectInput', '')
        phase =request.GET.get('phase', '')
        scale =request.GET.get('scaleInput', '')
        type =request.GET.get('domainInput', '')
        hot_position = request.GET.get('hot_position')

        print(city+distinct+work_exp+edu_exp)

        objects = PositionInfo.objects
        if city:
            objects = objects.filter(city=city)
        if distinct:
            objects = objects.filter(distinct=distinct)
        if work_exp:
            objects = objects.filter(work_exp=work_exp)
        if edu_exp:
            objects = objects.filter(edu_exp=edu_exp)
        if phase:
            objects = objects.filter(phase=phase)
        if scale:
            orginfo = OrgInfo.objects.filter(scale=scale)
            objects = objects.filter(org=orginfo).all()
        if type:
            objects = objects.filter(type=type)
        if hot_position:
            hot_positionme = objects.filter(name__icontains=hot_position)

        if kword:
            # Q是SQL语句里的or语法
            position_info = objects.filter(Q(name__icontains=kword) | Q(type__icontains=kword)).all()
        else:
            position_info = objects.order_by('-create_datetime').all()[:500]


        # 分页功能
        paginator = Paginator(position_info, 15)
        try:
            position_list = paginator.page(page)

            for position in position_list:
                tags = position.org.tags.split(',')
                position.tags = tags

                post_time = position.create_datetime

                now = datetime.datetime.now()
                timedelta = (now - post_time).days
                position.timedelta = timedelta

            # position_companys = {}
            # for one_position in  position_list:
            #     org = one_position.org
            #     position_company = {}
            #     position_company['tags'] = org.tags.split(',')
            #     position_companys[one_position.id] = position_company
        #
        except PageNotAnInteger:
            position_list = paginator.page(1)
        except EmptyPage:
            position_list = paginator.page(paginator.num_pages)

        position_exist = PositionInfo.objects.filter(name=kword)
        if position_exist:
            position_id = position_exist[0].id
            dynamic_position_info = Dynamic_Position.objects.filter(position_info_id=position_id).first()

            if dynamic_position_info:
                dynamic_position_info.dynamic_search += 1
                dynamic_position_info.save()

            else:
                dynamic = Dynamic_Position(dynamic_search=1, position_info_id=position_id)
                dynamic.save()
        return render(request, 'searchcomlist2.html', locals())
    else:
        # 处理POST请求，并重定向搜索页面。
        request.session['search_input'] = request.POST.get('search_input', '')

        print(request.POST)

        return redirect('/search/')


def companyView(request):
    user = request.user  # 可能为匿名用户
    if user.is_active:  # 如果不是匿名用户
        if user.userinfo_set.all().first():
            logined = True
            user_real_name = user.userinfo_set.all().first().name
        else:
            logined = False
    else:
        logined = False

    all_org = OrgInfo.objects.all()



    return render(request,'companylist.html',locals())

# 职位详情页
def jobinfoView(request):
    # user = request.user
    # if user.is_active:
    #     logined = True
    #     user_real_name = user.userinfo_set.all().first().name
    # else:
    #     logined = False
    return render(request, 'jobinfo.html',locals())


#查看更多
def searchmoreView(request):
    user = request.user
    if user.is_active:
        logined = True
        user_real_name = user.userinfo_set.all().first().name
    else:
        logined = False
    hot_position = Dynamic_Position.objects.select_related('position_info').order_by('-dynamic_search').all()
    latest = PositionInfo.objects.order_by('-create_datetime').all()
    return render(request,'searchcomlist.html',locals())
