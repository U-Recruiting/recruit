from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from index.models import *
from django.contrib.auth.decorators import login_required
from urllib.parse import unquote


def searchView(request, page):

    if request.method == 'GET':

        kword = request.session.get('search_input', '')
        print(kword)

        city =request.GET.get('city', '')
        distinct =request.GET.get('distinct', '')
        work_exp =request.GET.get('work_exp', '')
        edu_exp =request.GET.get('edu_exp', '')
        phase =request.GET.get('phase', '')
        scale =request.GET.get('scale', '')
        type =request.GET.get('type', '')

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
            objects = objects.filter(scale=scale)
        if type:
            objects = objects.filter(type=type)

        if kword:
            # Q是SQL语句里的or语法
            position_info = objects.filter(Q(name__icontains=kword) | Q(tags__icontains=kword)).all()
        else:
            position_info = objects.order_by('-create_datetime').all()[:50]
        # 分页功能
        # paginator = Paginator(position_info, 5)
        # try:
        #     contacts = paginator.page(page)
        # except PageNotAnInteger:
        #     contacts = paginator.page(1)
        # except EmptyPage:
        #     contacts = paginator.page(paginator.num_pages)

        position_exist = PositionInfo.objects.filter(name__icontains=kword)
        if position_exist:
            position_id = position_exist[0].id
            dynamic_position_info = Dynamic_Position.objects.filter(position_info_id=int(position_id)).first()

            if dynamic_position_info:
                dynamic_position_info.dynamic_search += 1
                dynamic_position_info.save()

            else:
                dynamic = Dynamic_Position(dynamic_search=1, position_info_id=position_id)
                dynamic.save()
        return render(request, 'searchcomlist.html', locals())
    else:
        # 处理POST请求，并重定向搜索页面。
        request.session['search_input'] = request.POST.get('search_input', '')
        return redirect('/search/1')


def companyView(request):
    current_user = request.user
    return render(request,'companylist.html',locals())
