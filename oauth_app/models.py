from django.db import models

# Create your models here.
class tipoUsu (models.Model):
    idUsu = models.IntegerField(primary_key=True,verbose_name='id')
    nomTipo = models.CharField(max_length=30, verbose_name= 'Tipo Usuario')

    def __str__(self):
        return self.nomTipo 

class Usuario(models.Model):
    correo = models.CharField(primary_key=True,max_length=120,verbose_name='Correo')
    password = models.CharField(max_length=60, verbose_name='Clave')
    personaNom = models.CharField(max_length=120, verbose_name='Nombre Persona')
    apellido = models.CharField(max_length=120, verbose_name='Apellido Completo')
    numTelefono = models.IntegerField(verbose_name='Numero Telefono')
    direccion = models.CharField(max_length=120, verbose_name='Direccion')
    tipoUsu = models.ForeignKey(tipoUsu, on_delete=models.CASCADE, verbose_name='Tipo Usuario')
    

    def __str__(self):
        return self.correo