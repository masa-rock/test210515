# from test_app.views import real_result
from typing import Text
from django.forms.models import ModelChoiceField
from test_app.models import Realsimulation_result_v1
from django.forms import ModelChoiceField
from django import forms
from django.db.models.query import QuerySet
from django.db.models import Count
from datetime import datetime as dt

# 210619_プルダウンメニューに買いの日が入るように指定したクラス
class MyModelChoiceField(ModelChoiceField):
  def label_from_instance(self,obj):
    datetime = dt.strftime(obj.Buy_date,'%Y/%m')
    return "%s" % datetime

class InputForm(forms.Form):
  pulldown = Realsimulation_result_v1.objects.extra(select={'day':'date(Realsimulation_result_v1.Buy_date)'}).values('day').annotate(available=Count('Buy_date'))
  pulldown_bar = MyModelChoiceField(label="日付",queryset=pulldown)
  # pulldown = MyModelChoiceField(label="日付",queryset=Realsimulation_result_v1.objects.all().distinct("Buy_date"))
  # sell_pattern = ModelChoiceField(label="売りパターン",queryset=Realsimulation_result_v1.objects.all().distinct("Sell_pattern"))

# class TextForm(forms.Form):
#   name = forms.CharField(label="名前",widget=forms.TextInput(attrs={'class':'form-control'}))
#   message = forms.CharField(label='内容',widget=forms.Textarea(attrs={'class':'form-control'}) )
