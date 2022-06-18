# Generated by Django 4.0.4 on 2022-05-18 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignatura',
            fields=[
                ('codAsignatura', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id')),
                ('nombreAsignatura', models.CharField(max_length=50, verbose_name='Categoría')),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellidoPat', models.CharField(blank=True, max_length=20, null=True, verbose_name='Apelido Paterno')),
                ('apellidoMat', models.CharField(blank=True, max_length=20, null=True, verbose_name='Apelido Materno')),
                ('correo', models.CharField(blank=True, max_length=30, null=True, verbose_name='Correo')),
                ('imagen', models.ImageField(null=True, upload_to='login/static/login/users', verbose_name='Imagen')),
                ('codAsignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.asignatura')),
            ],
        ),
    ]
