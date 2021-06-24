# from test_app.views import real_result
from django.forms.models import ModelChoiceField
from test_app.models import Realsimulation_result_v1
from django.forms import ModelChoiceField
from django import forms
from django.db.models.query import QuerySet
from datetime import datetime as dt

# 210619_プルダウンメニューに買いの日が入るように指定したクラス
class MyModelChoiceField(ModelChoiceField):
  def label_from_instance(self,obj):
    datetime = dt.strftime(obj.Buy_date,'%Y/%m')
    return "%s" % datetime

class InputForm(forms.Form):
  # pulldown = Realsimulation_result_v1.objects.annotate("Buy_Date")
  pulldown = MyModelChoiceField(label="日付",queryset=Realsimulation_result_v1.objects.all().distinct("Buy_date"))
  # sell_pattern = ModelChoiceField(label="売りパターン",queryset=Realsimulation_result_v1.objects.all().distinct("Sell_pattern"))