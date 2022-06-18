from os import stat
from xml.dom.minidom import Document
from django.urls import URLPattern, path
from .views import equipo,agregarDocente,modificarDocente,eliminarDocente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',equipo,name="equipo"),
    path('agregarDocente',agregarDocente,name="agregarDocente"),
    path('modificar_docente/<id>',modificarDocente,name="modificarDocente"),
    path('eliminarDocente/<id>',eliminarDocente,name="eliminarDocente"),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)