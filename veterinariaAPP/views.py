from django.shortcuts import render
#Llamar modelos
from veterinariaAPP.models import ingresoDueño,ingresoMascota,consulta,esteticaVeterinaria,vacunas,cirugias
from veterinariaAPP.forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def viewDuenos(request):
    return render(request, 'viewDuenos.html')