# Generated by Django 4.1.1 on 2022-11-20 23:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinariaAPP', '0004_rename_nombre_dueño_ingresodueno_nombre'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingresomascota',
            old_name='nombreMascota',
            new_name='nombre_mascota',
        ),
    ]
