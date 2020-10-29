from django.urls import path,include
from . import views

urlpatterns =[
    path('post',views.index,name='post'),
    path('<int:id>/detail',views.detail,name='detail'),
    path('',views.anasayfa,name='anasayfa'),
    path('report',views.report,name='report'),
]