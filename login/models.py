from django.db import models

# Create your models here.
class TipoUsuario(models.Model):
    idUsuario = models.IntegerField(primary_key=True,verbose_name='Id')
    nombreTipo = models.CharField(max_length=50,verbose_name='Categoría')

    def __str__(self):
        return self.nombreTipo


class Usuario(models.Model):
    rut = models.CharField(max_length=15,primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=20, verbose_name='Nombre')
    apellidoPat = models.CharField(max_length=20,null=True, blank=True, verbose_name='Apelido Paterno')
    apellidoMat = models.CharField(max_length=20,null=True, blank=True, verbose_name='Apelido Materno')
    password = models.CharField(max_length=20, verbose_name='Contraseña')
    correo = models.CharField(max_length=30,null=True, blank=True, verbose_name='Correo')
    imagen= models.ImageField(upload_to="login/static/login/users",null=True, height_field=None, width_field=None, max_length=None, verbose_name='Imagen')
    idUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.rut
