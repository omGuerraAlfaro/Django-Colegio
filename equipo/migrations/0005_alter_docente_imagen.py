# Generated by Django 4.0.4 on 2022-06-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0004_alter_docente_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='equipo/static/equipo/Docentes', verbose_name='Imagen'),
        ),
    ]
