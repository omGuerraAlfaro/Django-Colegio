from os import stat
from xml.dom.minidom import Document
from django.urls import URLPattern, path
from .views import listar_libros,agregarLibro,modificarLibro,eliminarLibro
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',listar_libros,name="listar_libros"),
    path('agregarLibro',agregarLibro,name="agregarLibro"),
    path('modificarLibro/<id>',modificarLibro,name="modificarLibro"),
    path('eliminarLibro/<id>',eliminarLibro,name="eliminarLibro"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)