from django.db import models

# Create your models here.
class Asignatura(models.Model):
    codAsignatura = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreAsignatura = models.CharField(max_length=50,verbose_name='Categoría')

    def __str__(self):
        return self.nombreAsignatura


class Docente(models.Model):
    rut = models.CharField(max_length=15,primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellidoPat = models.CharField(max_length=20,null=True, verbose_name='Apelido Paterno')
    apellidoMat = models.CharField(max_length=20,null=True, verbose_name='Apelido Materno')
    correo = models.CharField(max_length=30,null=True, verbose_name='Correo')
    imagen= models.ImageField(upload_to="equipo/static/equipo/Docentes",null=True, blank=True, height_field=None, width_field=None, max_length=None, verbose_name='Imagen')
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
