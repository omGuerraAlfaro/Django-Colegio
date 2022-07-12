from django.db import models

# Create your models here.

class Libro(models.Model):
    sku = models.AutoField(primary_key=True, verbose_name='id')
    autor = models.CharField(max_length=100,null=True, verbose_name='Nombre autor')
    nombreLibro = models.CharField(max_length=100,null=True, verbose_name='Nombre libro')
    genero = models.CharField( max_length=50,verbose_name='Nombre genero')
    dias =  models.IntegerField(verbose_name='Dias prestamo')
    
    def __str__(self):
        return self.nombreLibro