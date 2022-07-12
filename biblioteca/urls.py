from os import stat
from xml.dom.minidom import Document
from django.urls import URLPattern, path
from .views import agregar_producto, eliminar_producto, limpiar_carrito, listar_libros,agregarLibro,modificarLibro,eliminarLibro, restar_producto,tienda,solicitar_Libros,historial,devolucion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',listar_libros,name="listar_libros"),
    path('agregarLibro',agregarLibro,name="agregarLibro"),
    path('modificarLibro/<id>',modificarLibro,name="modificarLibro"),
    path('eliminarLibro/<id>',eliminarLibro,name="eliminarLibro"),
    path('tienda/', tienda, name="Tienda"),
    path('solicitar_Libros/', solicitar_Libros, name="solicitar_Libros"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('historial/', historial, name="historial"),
    path('historial/devolver/<cod_prestamo>', devolucion, name="devolucion"),
    
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


    
    
    