# Generated by Django 4.1.1 on 2022-11-20 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinariaAPP', '0002_alter_cirugias_options_alter_consulta_options_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ingresoDueño',
            new_name='ingresoDueno',
        ),
        migrations.RenameField(
            model_name='ingresodueno',
            old_name='nombreDueño',
            new_name='nombre_Dueño',
        ),
    ]
