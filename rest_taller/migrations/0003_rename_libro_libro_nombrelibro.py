# Generated by Django 4.0.4 on 2022-06-27 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_taller', '0002_genero_libro_delete_docente_delete_taller'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='libro',
            new_name='nombreLibro',
        ),
    ]
