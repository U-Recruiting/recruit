from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .spider import LaGou

def spider(request):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city={0}&needAddtionalResult=false'
    la = LaGou(url=url)
    la.get_data_from_url()
    la.save_data_to_database()
    return HttpResponse('success!!!')