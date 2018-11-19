from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .spider import LaGou
from .spider2 import GaLouOrg
def spider(request):
    url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city={0}&needAddtionalResult=false'
    la = LaGou(url=url)
    la.get_data_from_url()
    la.save_data_to_database()
    return HttpResponse('success!!!')


def spider2(request):
    url = 'https://www.lagou.com/gongsi/{0}.html'
    la2 = GaLouOrg(url=url)
    la2.complete_org_info()
    return HttpResponse('successsss')