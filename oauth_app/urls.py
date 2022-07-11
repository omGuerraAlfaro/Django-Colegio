from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from .views import LoginGoogle, add_user, RegistrarUser
from rest_taller.viewsLogin import loginApi


urlpatterns = [
    #...
    path('loginGoogle',LoginGoogle,name="loginGoogle"),
    path('registrarUser',RegistrarUser,name="registrarUser"),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="loginGoogle.html")),
    path('logout', LogoutView.as_view(), name="logoutGoogle"),    
    path('agregar_usuarios',add_user,name="agregaruser"),

    
]