from django.shortcuts import render
from django.http import HttpResponse
from index.models import PositionInfo
# Create your views here.


def details(request, position_id):

    position_info_detail = PositionInfo.objects.get(id=position_id)

    return render(request, 'position_test.html', locals())