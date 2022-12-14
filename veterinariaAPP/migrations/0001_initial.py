# Generated by Django 4.1.1 on 2022-11-19 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ingresoDueño',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreDueño', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ingresoMascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreMascota', models.CharField(max_length=50)),
                ('edad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('dueño', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.ingresodueño')),
            ],
        ),
        migrations.CreateModel(
            name='vacunas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAtencion', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('tratamiento', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('nombrePaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.ingresomascota')),
            ],
        ),
        migrations.CreateModel(
            name='esteticaVeterinaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAtencion', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('tratamiento', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('nombrePaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.ingresomascota')),
            ],
        ),
        migrations.CreateModel(
            name='consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAtencion', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('tratamiento', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('nombrePaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.ingresomascota')),
            ],
        ),
        migrations.CreateModel(
            name='cirugias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaAtencion', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.CharField(max_length=100)),
                ('diagnostico', models.CharField(max_length=100)),
                ('tratamiento', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('nombrePaciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinariaAPP.ingresomascota')),
            ],
        ),
    ]
