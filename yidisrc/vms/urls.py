from django.urls import path,re_path

from . import views

urlpatterns = [
    path('vmslist/', views.vmslist, name='vmslist'),
    path('vmsadd/', views.vmsadd, name='vmsadd'),
]