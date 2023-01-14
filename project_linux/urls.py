from django.urls import path

from . import views

# définir les routes qui permettent d'accéder aux pages de l'application
urlpatterns = [
    path('', views.home, name='home'),
    path('gaz', views.gaz_function, name='gaz_function'),
    path('electricite', views.electricity_function, name='electricity_function'),
    path('combinegaz', views.gazCombine_function, name='gazCombine_function'),
]