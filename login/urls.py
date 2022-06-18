from django.urls import URLPattern, path
from .views import login,intranet

urlpatterns = [
    path('',login,name="login"),
    path('intranet',intranet,name="intranet"),
] 