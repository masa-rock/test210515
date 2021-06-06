from django.urls import path
from . import views

app_name="test_app"

urlpatterns = [
    path('',views.index),
    path('real/',views.realsimulation,name="real"),
    path('fanda/',views.fandamental,name="fanda"),
    path('fandaall/',views.fandamental_all,name="fanda_all"),
    path('fandatest1/',views.fandamental_test1,name="fanda_test1"),
]
