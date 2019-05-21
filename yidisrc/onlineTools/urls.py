from django.urls import path,re_path

from . import views

urlpatterns = [
    path('unicodeTransfer/', views.unicodeTransfer, name='unicodeTransfer'),
    path('md5Transfer/', views.md5Transfer, name='md5Transfer'),
]