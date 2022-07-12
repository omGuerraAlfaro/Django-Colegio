from django.contrib import admin

from biblioteca.models import Producto
from biblioteca.models import Prestamo
# Register your models here.
admin.site.register(Producto)
admin.site.register(Prestamo)