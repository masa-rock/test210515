from django.shortcuts import render
from .models import Fanda, Realsimulation_v1
from django.template.response import TemplateResponse
from django.db.models import F

# Create your views here.
def index(request):
  return TemplateResponse(request,'test_app/index.html')

def realsimulation(request):
    # stock = Realsimulation.objects.order_by("-date")[:12]

    # condition = {
    #     'date':stock[0].date,
    #     'close__gt':F('bb'),
    #     'days150__gt':F('days200')
    # }
    # datas = Realsimulation.objects.all().filter(**condition)
    datas = Realsimulation_v1.objects.all()

    return render(request,"test_app/real.html",{'datas': datas})

def fandamental(request):
    # condition = {
    #     'date':stock[0].date,
    #     'close__gt':F('bb'),
    #     'days150__gt':F('days200')
    # }
    # datas = Realsimulation.objects.all().filter(**condition)
    # datas = Fanda.objects.all()

    return render(request,"test_app/fanda.html")

def fandamental_all(request):
    # condition = {
    #     'date':stock[0].date,
    #     'close__gt':F('bb'),
    #     'days150__gt':F('days200')
    # }
    # datas = Realsimulation.objects.all().filter(**condition)
    datas = Fanda.objects.all()

    return render(request,"test_app/fanda_all.html",{'datas': datas})

def fandamental_test1(request):
    # condition = {
    #     'rieki_jousyou_0__gte':F("rieki_jousyou_1")
    # }
    datas = Fanda.objects.all().filter(rieki_jousyou_0__gte = 60)
    counter = datas.count()
    return render(request,"test_app/fanda_test1.html",{'datas': datas,
    'counter':counter
    })