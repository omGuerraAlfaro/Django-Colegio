# Generated by Django 4.0.4 on 2022-05-18 20:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='docente',
            old_name='codAsignatura',
            new_name='asignatura',
        ),
    ]
