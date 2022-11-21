from django import forms 
from django.forms import ModelForm
from .models import ingresoDueno, ingresoMascota, consulta, esteticaVeterinaria,vacunas,cirugias

class duenoForm(forms.Form):
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    

    def clean_nombre(self):
        nombre = self.cleander_data.get['nombre']
        if len(nombre) < 4:
            raise forms.ValidationError("el nombre debe tener al menos 4 caracteres")
    """ Despues de esto crear views.py """
class duenoForm(ModelForm):
    class Meta:
        model = ingresoDueno
        fields = '__all__'
        
    nombre = forms.CharField(max_length=50)
    edad = forms.IntegerField()    

class mascotaForm(forms.Form):
    nombre_mascota = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dueño = forms.ModelChoiceField(queryset=ingresoDueno.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class mascotaForm(ModelForm):
    class Meta:
        model = ingresoMascota
        fields = '__all__'

    nombre_mascota = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    dueño = forms.ModelChoiceField(queryset=ingresoDueno.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    edad = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

class consultaForm(forms.Form):
    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class consultaForm(ModelForm):
    class Meta:
        model = consulta
        fields = '__all__'
    
    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class esteticaForm(forms.Form):

    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class esteticaForm(ModelForm):
    class Meta:
        model = esteticaVeterinaria
        fields = '__all__'

    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 



class vacunaForm(forms.Form):

    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class vacunaForm(ModelForm):
    class Meta:
        model = vacunas
        fields = '__all__'

    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 


class cirugiaForm(forms.Form):

    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

class cirugiaForm(ModelForm):
    class Meta:
        model = cirugias
        fields = '__all__'

    nombre_paciente = forms.ModelChoiceField(queryset=ingresoMascota.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    fecha_atencion = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    motivo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    diagnostico = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tratamiento = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    observaciones = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    valor = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'})) 

