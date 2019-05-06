from django.urls import path,re_path

from . import views

urlpatterns = [
    path('common/', views.commonSecKnowledge, name='commonSecKnowledge'),
    path('web/', views.webSecKnowledge, name='webSecKnowledge'),
    path('app/', views.appSecKnowledge, name='appSecKnowledge'),
    path('app/editSecKnowledge/', views.editSecKnowledge, name='editSecKnowledge'),
    re_path(r'app/(?P<myid>[0-9]{1})/',views.pageEditSecKnowledge)
]