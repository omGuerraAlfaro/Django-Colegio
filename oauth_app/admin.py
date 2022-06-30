from django.contrib import admin
# Register your models here.
from .models import Usuario,tipoUsu
admin.site.register(Usuario)
admin.site.register(tipoUsu)