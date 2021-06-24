from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Fanda, Realsimulation_v1, Realsimulation_result_v1
from django.template.response import TemplateResponse
from django.db.models import F,Sum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import InputForm
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
    jousyouritu = 10
    condition ={
        "y_er_0__gt" : (jousyouritu/100+1)*F("y_er_1"),
        "y_er_1__gt" : (jousyouritu/100+1)*F("y_er_2"),
        "y_er_2__gt" : (jousyouritu/100+1)*F("y_er_3"),
        "y_er_3__gt" : (jousyouritu/100+1)*F("y_er_4"),
        "y_er_4__gt" : (jousyouritu/100+1)*F("y_er_5"),
    }
    datas = Fanda.objects.filter(**condition)
    counter = datas.count()
    paginator = Paginator(datas, 20)
    page = request.GET.get('page', 1)
    try:
    	pages = paginator.page(page)
    except PageNotAnInteger:
    	pages = paginator.page(1)
    except EmptyPage:
    	pages = paginator.page(1)
    return render(request,"test_app/fanda_all.html",{'pages':pages, 'counter':counter,})

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
        'rieki_jousyou_0__lte':50,
        'rieki_jousyou_1__lte':50,
        'rieki_jousyou_2__lte':50,
        'rieki_jousyou_3__gte':50,
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
    # Input_Form =InputForm()
    datas = Fanda.objects.all().filter(**condition)
    counter = datas.count()
    return render(request,"test_app/fanda_test3.html",{'datas': datas,
    'counter':counter,
    # 'Input_Form':Input_Form,
        })

def real_result(request):
    datas = Realsimulation_result_v1.objects.all()
    counter = datas.count()
    profit = datas.aggregate(Sum('Profit_and_lost'))["Profit_and_lost__sum"]
    Form =InputForm()
    # profit = profit['Profit_and_lost_sum']
    return render(request,"test_app/real_result.html",{'datas': datas,
    'counter':counter,
    'profit':profit,
    'form':Form,
    })

def result_squeeze(request):
    datas = Realsimulation_result_v1.objects.all()
    if request.method == 'POST':
        form = InputForm(request.POST)

        if form.is_valid():
            buy = form.cleaned_data.get("pulldown")
            if buy:
                data = datas.filter(Buy_date__contains=buy)
                print(buy)
                counter= data.count
                profit = data.aggregate(Sum('Profit_and_lost'))["Profit_and_lost__sum"]
    return  render(request,"test_app/real_result.html",{'datas': data,
    'counter':counter,
    'profit':profit,
    })