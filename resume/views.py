from django.shortcuts import render
from django.http import HttpResponse
from index.models import *
from PIL import Image
from django.conf import settings
import json
import os


# Create your views here.


def my_resume(request):
    current_user = request.user

    user_info = current_user.userinfo_set.all().first()

    work_exp = current_user.workexp_set.all().first()

    project_exp = current_user.projectexp_set.all().first()

    edu_exp = current_user.educationexp_set.all().first()

    hunting_intent = current_user.huntingintent_set.all().first()

    return render(request, 'myresume_test.html', locals())


def edit_userinfo(request):
    user = request.user
    userinfo = user.userinfo_set.all()
    if request.method == 'POST':
        name = request.POST.get('name', '')
        # birthday = request.POST.get('birthdayme', '')
        sex = request.POST.get('sex', '')
        print(sex)
        city = request.POST.get('city', '')
        phone = request.POST.get('phone', '')

        if name:
            userinfo.update(name=name)
        # if birthday:
        #     userinfo.update(birthday=birthday)
        if sex:
            userinfo.update(sex=sex)
        if city:
            userinfo.update(city=city)
        if phone:
            user.mobile = phone
        user.save()

        resp = {}
        resp['name'] = userinfo[0].name
        resp['birthday'] = userinfo[0].birthday
        resp['sex'] = userinfo[0].sex
        resp['city'] = userinfo[0].city
        resp['phone'] = user.mobile

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_workexp(request):
    user = request.user
    work_exp = user.workexp_set.all()
    if request.method == 'POST':

        company = request.POST.get('conpany', '')
        tag = request.POST.get('tag', '')
        department = request.POST.get('department', '')
        type = request.POST.get('type', '')
        position_name = request.POST.get('position_name', '')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        skill = request.POST.get('skill', '')
        description = request.POST.get('description', '')

        if company:
            work_exp.update(name=company)
        if tag:
            work_exp.update(tag=tag)
        if department:
            work_exp.update(name=department)
        if type:
            work_exp.update(department=type)
        if position_name:
            work_exp.update(position_name=position_name)
        if start_date:
            work_exp.update(start_date=start_date)
        if end_date:
            work_exp.update(end_date=end_date)
        if skill:
            work_exp.update(skill=skill)
        if description:
            work_exp.update(description=description)

        resp = {}
        resp['company'] = work_exp[0].company
        resp['tag'] = work_exp[0].tag
        resp['department'] = work_exp[0].department
        resp['type'] = work_exp[0].type
        resp['position_name'] = work_exp[0].position_name
        resp['start_date'] = work_exp[0].start_date
        resp['end_date'] = work_exp[0].end_date
        resp['skill'] = work_exp[0].skill
        resp['description'] = work_exp[0].description

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_projectexp(request):
    user = request.user
    project_exp = user.projectexp_set.all()

    if request.method == 'POST':
        name = request.POST.get('name', '')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        url = request.POST.get('url', '')
        description = request.POST.get('description', '')

        if name:
            project_exp.update(name=name)
        if start_date:
            project_exp.update(start_date=start_date)
        if end_date:
            project_exp.update(end_date=end_date)
        if url:
            project_exp.update(url=url)
        if description:
            project_exp.update(description=description)

        resp = {}
        resp['name'] = project_exp[0].name
        resp['start_date'] = project_exp[0].start_date
        resp['end_date'] = project_exp[0].end_date
        resp['url'] = project_exp[0].url
        resp['description'] = project_exp[0].description

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_educationexp(request):
    user = request.user
    education_exp = user.educationexp_set.all()

    if request.method == 'POST':
        school = request.POST.get('school', '')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        education = request.POST.get('education', '')  ##待改成char
        subject = request.POST.get('subject', '')

        if school:
            education_exp.update(school=school)
        if start_date:
            education_exp.update(start_date=start_date)
        if end_date:
            education_exp.update(end_date=end_date)
        if education:
            education_exp.update(education=education)
        if subject:
            subject.update(subject=subject)

        resp = {}
        resp['school'] = education_exp[0].school
        resp['start_date'] = education_exp[0].start_date
        resp['end_date'] = education_exp[0].end_date
        resp['education'] = education_exp[0].education
        resp['subject'] = education_exp[0].subject

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_huntingintent(request):
    user = request.user
    huntingintent_exp = user.huntingintent_set.all()

    if request.method == 'POST':
        position = request.POST.get('school', '')
        position_type = request.POST.get('school', '')
        city = request.POST.get('school', '')
        satrt_salary = request.POST.get('school', '')
        end_salary = request.POST.get('school', '')

        if position:
            huntingintent_exp.update(position=position)
        if position_type:
            huntingintent_exp.update(position_type=position)
        if city:
            huntingintent_exp.update(city=city)
        if satrt_salary:
            huntingintent_exp.update(satrt_salary=satrt_salary)
        if end_salary:
            huntingintent_exp.update(subject=end_salary)

        resp = {}
        resp['position'] = huntingintent_exp[0].position
        resp['position_type'] = huntingintent_exp[0].position_type
        resp['city'] = huntingintent_exp[0].city
        resp['satrt_salary'] = huntingintent_exp[0].satrt_salary
        resp['end_salary'] = huntingintent_exp[0].end_salary

    return HttpResponse(json.dumps(resp), content_type="application/json")


def edit_avatar(request):
    user = request.user
    userinfo = user.userinfo_set.all()
    if request.method == 'POST':
        avatar = request.FILES.get('avatar','')
        path = os.path.join(settings.BASE_DIR, 'static/avatar/'+str(user.id)+'.jpg')
        img = Image.open(avatar)
        img.save(path)
        print(img)
    img_path = 'avadar/'+str(user.id)+'.jpg'

    return render(request, 'edit_avatar.html', locals())