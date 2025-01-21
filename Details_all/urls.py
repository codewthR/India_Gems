from django.contrib import admin
from django.urls import path
from Details_all import views



urlpatterns = [
    path('sending_data', views.data_sending , name='sending_data'),
    path('getting_data', views.data_getting, name='getting_data'),
]