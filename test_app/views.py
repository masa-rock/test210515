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
    jousyouritu = 5
    condition ={
        "s_er_0__gt" : (jousyouritu/100+1)*F("s_er_4"),
        "s_er_1__gt" : (jousyouritu/100+1)*F("s_er_5"),
        "s_er_2__gt" : (jousyouritu/100+1)*F("s_er_6"),
        "s_er_3__gt" : (jousyouritu/100+1)*F("s_er_7"),
        "s_er_4__gt" : (jousyouritu/100+1)*F("s_er_8"),
        "s_er_5__gt" : (jousyouritu/100+1)*F("s_er_9"),
        "s_er_6__gt" : (jousyouritu/100+1)*F("s_er_10"),
        "s_er_7__gt" : (jousyouritu/100+1)*F("s_er_11"),
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
    return render(request,"test_app/fanda_test1.html",{'pages':pages, 'counter':counter,})

def fandamental_test2(request):
    jousyouritu = 10
    condition ={
        "y_u_0__gt" : (jousyouritu/100+1)*F("y_u_1"),
        "y_u_1__gt" : (jousyouritu/100+1)*F("y_u_2"),
        "y_u_2__gt" : (jousyouritu/100+1)*F("y_u_3"),
        "y_u_3__gt" : (jousyouritu/100+1)*F("y_u_4"),
        "y_u_4__gt" : (jousyouritu/100+1)*F("y_u_5"),
        "y_u_5__gt" : (jousyouritu/100+1)*F("y_u_6"),
        "y_u_6__gt" : (jousyouritu/100+1)*F("y_u_7"),
        "y_u_7__gt" : (jousyouritu/100+1)*F("y_u_8"),
        "y_u_8__gt" : (jousyouritu/100+1)*F("y_u_9"),
        "y_u_9__gt" : (jousyouritu/100+1)*F("y_u_10"),
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

    return render(request,"test_app/fanda_test2.html",{'pages':pages, 'counter':counter,})

def fandamental_test3(request):
    jousyouritu = 10
    condition ={
        "y_er_0__gt" : (jousyouritu/100+1)*F("y_er_1"),
        "y_er_1__gt" : (jousyouritu/100+1)*F("y_er_2"),
        "y_er_2__gt" : (jousyouritu/100+1)*F("y_er_3"),
        "y_er_3__gt" : (jousyouritu/100+1)*F("y_er_4"),
        "y_er_4__gt" : (jousyouritu/100+1)*F("y_er_5"),
        "y_er_5__gt" : (jousyouritu/100+1)*F("y_er_6"),
        "y_er_6__gt" : (jousyouritu/100+1)*F("y_er_7"),
        "y_er_7__gt" : (jousyouritu/100+1)*F("y_er_8"),
        "y_er_8__gt" : (jousyouritu/100+1)*F("y_er_9"),
        "y_er_9__gt" : (jousyouritu/100+1)*F("y_er_10"),
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

    return render(request,"test_app/fanda_test3.html",{'pages':pages, 'counter':counter,})

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