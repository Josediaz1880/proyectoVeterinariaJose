from django.db import models

# Create your models here.

#modelo para ingreso dueño
class ingresoDueño(models.Model):
    nombreDueño = models.CharField(max_length=50)
    edad = models.IntegerField()

    class Meta:
        verbose_name = "Nombre dueño"
        verbose_name_plural = "Nombre dueños"

    def __str__(self):
        return self.nombreDueño

#modelo para ingreso mascota
class ingresoMascota(models.Model):
    nombreMascota = models.CharField(max_length=50)
    dueño = models.ForeignKey(ingresoDueño, on_delete=models.CASCADE)
    edad = models.IntegerField()
    descripcion= models.CharField(max_length=100)

    class Meta:
        verbose_name = "Nombre mascota"
        verbose_name_plural = "Nombre mascotas"

    def __str__(self):
        return self.nombreMascota

#Modelo para consultas medicas 
class consulta(models.Model):
    nombrePaciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente

#modelo para estetica veterinaria
class esteticaVeterinaria (models.Model):
    nombrePaciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente

#modelo para vacunas
class vacunas(models.Model):
    nombrePaciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente

# modelo para cirugias
class cirugias(models.Model):
    nombrePaciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fechaAtencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "nombre paciente"
        verbose_name_plural = "nombre pacientes"

    def __str__(self):
        return self.nombrePaciente