# Generated by Django 4.0.4 on 2022-07-05 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_taller', '0005_alter_libro_genero_delete_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='sku',
            field=models.AutoField(primary_key=True, serialize=False, verbose_name='id'),
        ),
    ]
