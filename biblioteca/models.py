from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=64)
    precio = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
class Prestamo(models.Model):
    cod_prestamo =  models.IntegerField(primary_key=False, verbose_name='cod_Prestamo')
    lista_libros = models.CharField(max_length=200,verbose_name='lista')
    email = models.CharField(max_length=120,verbose_name='Correo')
    fechaDevolucion = models.DateTimeField(verbose_name="Fecha devolucion")
    estado = models.IntegerField(default=0, verbose_name="Estado")
    def __str__(self):
        return self.lista_libros
