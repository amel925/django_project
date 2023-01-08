from django.urls import path

from . import views

urlpatterns = [
    path('gaz', views.index, name='index'),
    path('electricite', views.index2, name='index2'),
]