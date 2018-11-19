from django.shortcuts import render
from django.http import HttpResponse
from index.models import PositionInfo
# Create your views here.


def delivery(request):

    # 当前用户
    user = request.user

    print(user)

    # 当前用户简历
    resume = user.resume_set.all()[0]

    # 简历所投岗位
    positions = resume.positioninfo_set.all()

    print(positions)

    return render(request, 'deliverybox_test.html', locals())


def mycollection(request):
    user = request.user
    print(user)
    collections = user.collection_set.all()

    print(collections)

    return render(request, 'collectionbox_test.html', locals())


def collect(request):
    pass

def companydetail(request):
    return render(request, 'companydetail.html')