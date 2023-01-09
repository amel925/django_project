from django.urls import path

from . import views

urlpatterns = [
    path('gaz', views.index, name='index'),
    path('electricite', views.index2, name='index2'),
    path('combinegaz', views.index3, name='index3'),
]