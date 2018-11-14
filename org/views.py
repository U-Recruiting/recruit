from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
from index.models import PositionInfo

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


def post_position(request):
    user = request.user
    # org_info = user.orginfo_set.all()[0]

    if request.method == 'POST':
        type = request.POST.get('type','')
        name = request.POST.get('name','')
        department = request.POST.get('department','')
        job_catagory = request.POST.get('job_catagory','')
        start_salary = request.POST.get('start_salary','')
        end_salary = request.POST.get('end_salary','')
        city = request.POST.get('city','')
        distinct = request.POST.get('distinct','')
        address = request.POST.get('address','')
        work_exp = request.POST.get('tywork_exppe','')
        edu_exp = request.POST.get('edu_exp','')
        tags = request.POST.get('tags','')
        desc = request.POST.get('desc','')
        positionAdvantage = request.POST.get('positionAdvantage','')
        subwayline = request.POST.get('subwayline','')
        linestaion = request.POST.get('subwalinestaionyline','')
        create_datetime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        position = PositionInfo(type=type,name=name,department=department,job_catagory=job_catagory,
                                start_salary=start_salary,end_salary=end_salary,city=city,distinct=distinct,
                                address=address,work_exp=work_exp,edu_exp=edu_exp,tags=tags,
                                desc=desc,positionAdvantage=positionAdvantage,subwayline=subwayline,
                                create_datetime=create_datetime)
        position.save()
        print(city)

    return render(request, 'post.html', locals())