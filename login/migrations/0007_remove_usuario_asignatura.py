# Generated by Django 4.0.4 on 2022-05-18 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_usuario_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='Asignatura',
        ),
    ]
