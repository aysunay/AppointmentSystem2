from django.urls import path
from . import views 
from .views import home
from Randevu.views import home

urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('create/', views.create_appointment, name='create_appointment'), 
    path('', home, name='home'), 
]