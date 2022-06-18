from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, verbose_name='Id')
    nombre_genero = models.CharField(max_length=50,verbose_name='Nombre genero')

    def __str__(self):
        return self.nombre_genero


class Libro(models.Model):
    sku = models.AutoField(primary_key=True, verbose_name='Rut')
    autor = models.CharField(max_length=100,null=True, verbose_name='Nombre autor')
    libro = models.CharField(max_length=100,null=True, verbose_name='Nombre libro')
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.libro