from django.urls import path
from . import views

urlpatterns = [
    path('', views.swiggy,name='home'),
    path('swiggy/',views.swiggy2,name='swiggy2')
]