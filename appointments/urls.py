from django.urls import path
from . import views 



urlpatterns = [
    path('', views.appointment_list, name='appointment_list'),
    path('create/', views.create_appointment, name='create_appointment'),
]
