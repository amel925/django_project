from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gaz', views.gaz_function, name='gaz_function'),
    path('electricite', views.electricity_function, name='electricity_function'),
    path('combinegaz', views.index3, name='index3'),
]