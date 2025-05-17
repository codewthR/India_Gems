from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_image, name='upload'),
    path('images/', views.view_images, name='images'),
    path('feed/', views.feed, name='feed'),
    path('like/', views.like_photo, name='like_photo'),
    path('comment/', views.add_comment, name='add_comment'),
]
