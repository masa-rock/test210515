from django.shortcuts import render
from .models import Fanda, Realsimulation_v1, Realsimulation_result_v1
from django.template.response import TemplateResponse
from django.db.models import F,Sum

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
    condition = {
        'rieki_jousyou_0__gte':100,
        'rieki_jousyou_1__gte':100,
        'rieki_jousyou_2__gte':40,
    }
    datas = Fanda.objects.all().filter(**condition)
    counter = datas.count()
    return render(request,"test_app/fanda_test1.html",{'datas': datas,
    'counter':counter
    })

def fandamental_test2(request):
    condition = {
        'rieki_jousyou_0__gte':10,
        'rieki_jousyou_1__gte':10,
        'rieki_jousyou_2__gte':10,
        'rieki_jousyou_3__gte':10,
    }
    datas = Fanda.objects.all().filter(**condition)
    counter = datas.count()
    return render(request,"test_app/fanda_test2.html",{'datas': datas,
    'counter':counter
    })

def fandamental_test3(request):
    condition = {
        'rieki_jousyou_0__gte':100,
        'rieki_jousyou_1__gte':100,
        'rieki_jousyou_2__gte':40,
        'uriage_jousyou_0__gte':0,
        'uriage_jousyou_1__gte':0,
        'uriage_jousyou_2__gte':0,
    }
    datas = Fanda.objects.all().filter(**condition)
    counter = datas.count()
    return render(request,"test_app/fanda_test3.html",{'datas': datas,
    'counter':counter
    })

def real_result(request):
    datas = Realsimulation_result_v1.objects.all()
    counter = datas.count()
    profit = datas.aggregate(Sum('Profit_and_lost'))["Profit_and_lost__sum"]
    # profit = profit['Profit_and_lost_sum']
    return render(request,"test_app/real_result.html",{'datas': datas,
    'counter':counter,
    'profit':profit,
    })