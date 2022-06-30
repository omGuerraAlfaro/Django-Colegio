from unicodedata import name
from django.urls import path
from .views import lista_taller, detalle_taller


urlpatterns = [
    path('lista_taller',lista_taller,name="lista_taller"),
    path('detalle_taller/<sku>',detalle_taller,name="detalle_taller"),
    
]