from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import LoginGoogle
from rest_taller.viewsLogin import loginApi


urlpatterns = [
    #...
    path('loginGoogle',LoginGoogle,name="loginGoogle"),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view(), name="logoutGoogle"),
    path('loginGoogle',loginApi,name='loginDjango'),
    

    
]