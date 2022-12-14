# Generated by Django 4.1.1 on 2022-11-21 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('veterinariaAPP', '0005_rename_nombremascota_ingresomascota_nombre_mascota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cirugias',
            old_name='fechaAtencion',
            new_name='fecha_atencion',
        ),
        migrations.RenameField(
            model_name='cirugias',
            old_name='nombrePaciente',
            new_name='nombre_paciente',
        ),
        migrations.RenameField(
            model_name='consulta',
            old_name='fechaAtencion',
            new_name='fecha_atencion',
        ),
        migrations.RenameField(
            model_name='consulta',
            old_name='nombrePaciente',
            new_name='nombre_paciente',
        ),
        migrations.RenameField(
            model_name='esteticaveterinaria',
            old_name='fechaAtencion',
            new_name='fecha_atencion',
        ),
        migrations.RenameField(
            model_name='esteticaveterinaria',
            old_name='nombrePaciente',
            new_name='nombre_paciente',
        ),
        migrations.RenameField(
            model_name='vacunas',
            old_name='fechaAtencion',
            new_name='fecha_atencion',
        ),
        migrations.RenameField(
            model_name='vacunas',
            old_name='nombrePaciente',
            new_name='nombre_paciente',
        ),
    ]
