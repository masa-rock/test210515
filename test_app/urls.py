from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name="test_app"

urlpatterns = [
    path('',views.index),
    path('real/',views.realsimulation,name="real"),
    path('fanda/',views.fandamental,name="fanda"),
    path('fandaall/',views.fandamental_all,name="fanda_all"),
    path('fandatest1/',views.fandamental_test1,name="fanda_test1"),
    path('fandatest2/',views.fandamental_test2,name="fanda_test2"),
    path('fandatest3/',views.fandamental_test3,name="fanda_test3"),
    path('real_result/',views.real_result,name="real_result"),
    path('result_squeeze',views.result_squeeze,name="result_squeeze"),
    path('index/',views.Index.as_view(), name="index"),
    path('detail/<pk>/',views.Detail.as_view(),name="detail"),
    path('create/',views.Create.as_view(), name="create"),
    path('update/<pk>',views.Update.as_view(), name="update"),
    path('delete/<pk>',views.Delete.as_view(), name="delete"),
]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)