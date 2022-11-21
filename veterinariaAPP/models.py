from django.db import models

# Create your models here.

#modelo para ingreso dueño
class ingresoDueno(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()

    class Meta:
        verbose_name = "Ingresar Dueño"
        verbose_name_plural = "Ingresar Dueños"

    def __str__(self):
        return self.nombre

#modelo para ingreso mascota
class ingresoMascota(models.Model):
    nombre_mascota = models.CharField(max_length=50)
    dueño = models.ForeignKey(ingresoDueno, on_delete=models.CASCADE)
    edad = models.IntegerField()
    descripcion= models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ingresar mascota"
        verbose_name_plural = "Ingresar mascotas"

    def __str__(self):
        return self.nombre_mascota

#Modelo para consultas medicas 
class consulta(models.Model):
    nombre_paciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "Ingresar consulta"
        verbose_name_plural = "Ingresar consultas"

    def __str__(self):
        return self.motivo

#modelo para estetica veterinaria
class esteticaVeterinaria(models.Model):
    nombre_paciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "Ingresar estetica veterinaria"
        verbose_name_plural = "Ingresar estetica veterinarias"

    def __str__(self):
        return self.motivo

#modelo para vacunas
class vacunas(models.Model):
    nombre_paciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "Ingresar vacuna"
        verbose_name_plural = "Ingresar vacunas"

    def __str__(self):
        return self.motivo

# modelo para cirugias
class cirugias(models.Model):
    nombre_paciente = models.ForeignKey(ingresoMascota, on_delete=models.CASCADE)
    fecha_atencion = models.DateTimeField(auto_now_add=True)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observaciones = models.CharField(max_length=100)
    valor = models.IntegerField() 

    class Meta:
        verbose_name = "Ingresar cirugia"
        verbose_name_plural = "Ingresar cirugias"

    def __str__(self):
        return self.motivo