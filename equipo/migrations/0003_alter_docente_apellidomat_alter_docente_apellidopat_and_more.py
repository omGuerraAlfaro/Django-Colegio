# Generated by Django 4.0.4 on 2022-05-19 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_rename_codasignatura_docente_asignatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='apellidoMat',
            field=models.CharField(max_length=20, null=True, verbose_name='Apelido Materno'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='apellidoPat',
            field=models.CharField(max_length=20, null=True, verbose_name='Apelido Paterno'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='correo',
            field=models.CharField(max_length=30, null=True, verbose_name='Correo'),
        ),
        migrations.AlterField(
            model_name='docente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='equipo/static/equipo/Docentes', verbose_name='Imagen'),
        ),
    ]
