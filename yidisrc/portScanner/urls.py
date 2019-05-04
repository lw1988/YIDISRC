from django.urls import path

from . import views

urlpatterns = [
    path('', views.portscanner, name='portscanner'),
    path('auto/', views.autoportscanner, name='autoportscanner'),
]