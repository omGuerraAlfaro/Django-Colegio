from django.urls import path
from .views import lista_taller, detalle_taller
from .viewsLogin import loginApi

urlpatterns = [
    path('lista_taller',lista_taller,name="lista_taller"),
    path('detalle_taller/<sku>',detalle_taller,name="detalle_taller"),
    path('loginApi',loginApi,name="loginApi"),
]