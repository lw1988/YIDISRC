from django.urls import path,re_path

from . import views

urlpatterns = [
    path('unicodeTransfer/', views.unicodeTransfer, name='unicodeTransfer'),
]