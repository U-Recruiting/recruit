from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.


@login_required(login_url='/user/login')
def home(request, org_id):
    return HttpResponse('hello'+str(org_id))



def post(request):

    user = request.user
    org_info = user.orginfo_set.all().first()

    if request.method == 'POST':
        pass
        # type =
        # name =
        # job_catagory =
        # start_salary =
        # end_salary =
        # city =
        #
        # distinct =
        #
        # address =
        # work_exp =
        # edu_exp =
        #
        # tags =
        #
        # desc =
        #
        # positionAdvantage =
        # subwayline =
        # linestaion =
        # create_datetime =


    return render(request, 'post.html', locals())