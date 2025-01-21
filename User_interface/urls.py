from django.contrib import admin
from django.urls import path, include
from User_interface import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('explore', views.city_all ,name='explore'),
    path('explore/<str:state_names>/', views.city_all ,name='exp')
]