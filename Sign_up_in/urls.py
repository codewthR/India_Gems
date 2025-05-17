from django.contrib import auth
from django.urls import path, include
from Sign_up_in import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('logging/', views.logging ,name='login'),
    path('signup/', views.signup, name='signup'),
    # path('forgot-password', views.forgot_password, name='forgot-password'),
    path('logout_page', views.logout_page, name='logout_page'),
    # path('forgot-password', views.forgotpass , name='forgot-password')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)