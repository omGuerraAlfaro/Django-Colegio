# Generated by Django 4.0.4 on 2022-05-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_usuario_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Rut'),
        ),
    ]