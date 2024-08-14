from django.urls import path
from .views import home, to_home

urlpatterns = [
    path('', to_home, name='to_home'),
    path('home', home, name='home'),
]
