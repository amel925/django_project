from django.urls import path

from . import views

urlpatterns = [
    path('', views.index2, name='index'),
    #path('hell', views.index2, name='index2'),
]