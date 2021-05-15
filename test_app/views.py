from django.shortcuts import render
from .models import Realsimulation
from django.template.response import TemplateResponse
from django.db.models import F

# Create your views here.
def index(request):
  return TemplateResponse(request,'test_app/index.html')

def realsimulation(request):
    stock = Realsimulation.objects.order_by("-date")[:12]

    condition = {
        'date':stock[0].date,
        'close__gt':F('bb'),
        'days150__gt':F('days200')
    }
    datas = Realsimulation.objects.all().filter(**condition)

    return render(request,"test_app/real.html",{'datas': datas})
