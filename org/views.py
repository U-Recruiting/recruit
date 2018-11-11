from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/user/login')
def home(request, org_id):
    return HttpResponse('hello'+str(org_id))