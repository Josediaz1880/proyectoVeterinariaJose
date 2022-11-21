from django.shortcuts import render, redirect
#Llamar modelos
from veterinariaAPP.models import ingresoDueno,ingresoMascota,consulta,esteticaVeterinaria,vacunas,cirugias
from veterinariaAPP.forms import *
from django.db.models import Avg, Sum, Min, Max, Count

# Create your views here.
def index(request):
    return render(request, 'index.html')

def viewDuenos(request):
    listaDuenos = ingresoDueno.objects.all()
    total = ingresoDueno.objects.all().aggregate(Count('nombre'))

    data={
        'dueno':listaDuenos,
        'total': total}
    return render(request, 'viewDuenos.html',data )

def viewMascotas(request):
    listaMascotas = ingresoMascota.objects.all()

    total = ingresoMascota.objects.all().aggregate(Count('nombre_mascota'))

    
    data={
        'mascota':listaMascotas,
        'total': total
 }
    return render(request, 'viewMascotas.html',data)

def viewConsultas(request):
    listaConsultas = consulta.objects.all()

    """ promedio de los precios """
    promedio = consulta.objects.all().aggregate(Avg('valor'))
    """ Suma de los precios """
    suma = consulta.objects.all().aggregate(Sum('valor'))
    """ total elementos """
    total = consulta.objects.all().aggregate(Count('valor'))
    """ precio mas alto """
    maximo = consulta.objects.all().aggregate(Max('valor'))
    """ Precio más bajo """
    minimo = consulta.objects.all().aggregate(Min('valor'))

    data={
        'consulta':listaConsultas,
        'promedio' : promedio,
        'suma' : suma,
        'total': total,
        'maximo' : maximo,
        'minimo' : minimo        
    }

    return render(request, 'viewConsultas.html', data)

def viewEstetica(request):
    listaEstetica = esteticaVeterinaria.objects.all()

    """ promedio de los precios """
    promedio = esteticaVeterinaria.objects.all().aggregate(Avg('valor'))
    """ Suma de los precios """
    suma = esteticaVeterinaria.objects.all().aggregate(Sum('valor'))
    """ total elementos """
    total = esteticaVeterinaria.objects.all().aggregate(Count('valor'))
    """ precio mas alto """
    maximo = esteticaVeterinaria.objects.all().aggregate(Max('valor'))
    """ Precio más bajo """
    minimo = esteticaVeterinaria.objects.all().aggregate(Min('valor'))

    data = {
        'estetica':listaEstetica,
        'promedio' : promedio,
        'suma' : suma,
        'total': total,
        'maximo' : maximo,
        'minimo' : minimo  }
    return render(request, 'viewEstetica.html',data)

def viewVacunas(request):
    listaVacuna = vacunas.objects.all()

    """ promedio de los precios """
    promedio = vacunas.objects.all().aggregate(Avg('valor'))
    """ Suma de los precios """
    suma = vacunas.objects.all().aggregate(Sum('valor'))
    """ total elementos """
    total = vacunas.objects.all().aggregate(Count('valor'))
    """ precio mas alto """
    maximo = vacunas.objects.all().aggregate(Max('valor'))
    """ Precio más bajo """
    minimo = vacunas.objects.all().aggregate(Min('valor'))

    data={
        'vacuna':listaVacuna,
        'promedio' : promedio,
        'suma' : suma,
        'total': total,
        'maximo' : maximo,
        'minimo' : minimo  }
    return render(request, 'viewVacunas.html',data)

def viewCirugias(request):
    listaCirugia = cirugias.objects.all()

    """ promedio de los precios """
    promedio = cirugias.objects.all().aggregate(Avg('valor'))
    """ Suma de los precios """
    suma = cirugias.objects.all().aggregate(Sum('valor'))
    """ total elementos """
    total = cirugias.objects.all().aggregate(Count('valor'))
    """ precio mas alto """
    maximo = cirugias.objects.all().aggregate(Max('valor'))
    """ Precio más bajo """
    minimo = cirugias   .objects.all().aggregate(Min('valor'))

    data={
        'cirugia':listaCirugia,
        'promedio' : promedio,
        'suma' : suma,
        'total': total,
        'maximo' : maximo,
        'minimo' : minimo }
    return render(request, 'viewCirugias.html', data)

def crearDueno(request): 
    form = duenoForm()
    if (request.method == 'POST'):
        form = duenoForm(request.POST)
        if form.is_valid():
            due= form.cleaned_data
            dueno = ingresoDueno(
                nombre = due['nombre'],
                edad = due['edad']
            )
            print ("datos validos")
            dueno.save()
            form = ''
            return redirect("/duenos")
    data = {'form': form, 'titulo': 'Ingresar Dueño'}
    return render(request, 'crearDueno.html', data)

def crearMascota(request): 
    form = mascotaForm()
    if (request.method == 'POST'):
        form = mascotaForm(request.POST)
        if form.is_valid():
            masc= form.cleaned_data
            mascota = ingresoMascota(
                nombre_mascota = masc['nombre_mascota'],
                dueño = masc['dueño'],
                edad = masc['edad'],
                descripcion = masc['descripcion']
            )
            print ("datos validos")
            mascota.save()
            form = ''
            return redirect("/mascotas")
    data = {'form': form, 'titulo': 'Ingresar Mascota'}
    return render(request, 'crearMascota.html', data)

def crearConsulta(request): 
    form = consultaForm()
    
    if (request.method == 'POST'):
        form = consultaForm(request.POST)
        if form.is_valid():
            con= form.cleaned_data
            consul = consulta(
                nombre_paciente = con['nombre_paciente'],
                fecha_atencion = con['fecha_atencion'],
                motivo = con['motivo'],
                diagnostico = con['diagnostico'],
                tratamiento = con['tratamiento'],
                observaciones = con['observaciones'],
                valor = con['valor'],
            )
            print ("datos validos")
            consul.save()
            form = ''
            return redirect("/consultas")
    data = {'form': form, 'titulo': 'Ingresar Consulta'}
    return render(request, 'crearConsulta.html', data)

def crearEstetica(request):
    form = esteticaForm()
    if (request.method == 'POST'):
        form = esteticaForm(request.POST)
        if form.is_valid():
            este= form.cleaned_data
            estetica = esteticaVeterinaria(
                nombre_paciente = este['nombre_paciente'],
                fecha_atencion = este['fecha_atencion'],
                motivo = este['motivo'],
                diagnostico = este['diagnostico'],
                tratamiento = este['tratamiento'],
                observaciones = este['observaciones'],
                valor = este['valor'],
            )
            print ("datos validos")
            estetica.save()
            form = ''
            return redirect("/estetica")
    data = {'form': form, 'titulo': 'Ingresar hora estetica'}
    return render(request, 'crearEstetica.html', data)


def crearVacuna(request): 
    form = consultaForm()
    
    if (request.method == 'POST'):
        form = vacunaForm(request.POST)
        if form.is_valid():
            vac= form.cleaned_data
            vacuna = vacunas(
                nombre_paciente = vac['nombre_paciente'],
                fecha_atencion = vac['fecha_atencion'],
                motivo = vac['motivo'],
                diagnostico = vac['diagnostico'],
                tratamiento = vac['tratamiento'],
                observaciones = vac['observaciones'],
                valor = vac['valor'],
            )
            print ("datos validos")
            vacuna.save()
            form = ''
            return redirect("/vacunas")
    data = {'form': form, 'titulo': 'Ingresar Vacuna'}
    return render(request, 'crearVacuna.html', data)

def crearCirugia(request): 
    form = cirugiaForm()   
    if (request.method == 'POST'):
        form = cirugiaForm(request.POST)
        if form.is_valid():
            ciru= form.cleaned_data
            cirugia = cirugias(
                nombre_paciente = ciru['nombre_paciente'],
                fecha_atencion = ciru['fecha_atencion'],
                motivo = ciru['motivo'],
                diagnostico = ciru['diagnostico'],
                tratamiento = ciru['tratamiento'],
                observaciones = ciru['observaciones'],
                valor = ciru['valor'],
            )
            print ("datos validos")
            cirugia.save()
            form = ''
            return redirect("/cirugias")
    data = {'form': form, 'titulo': 'Ingresar Cirugía'}
    return render(request, 'crearCirugia.html', data)

def editarDueno(request,id):
    dueno = ingresoDueno.objects.get(id=id)
    data = {
        'form' : duenoForm(instance=dueno),
        'titulo' : 'Editar Dueño'
    }
    if (request.method == 'POST'):
        form = duenoForm( request.POST,instance=dueno)
        if (form.is_valid()):
            form.save()
            return redirect("/duenos")
        else: 
            data['form'] = form
    return render(request, 'crearDueno.html', data)

def editarMascota(request,id):
    mascota = ingresoMascota.objects.get(id=id)
    data = {
        'form' : mascotaForm(instance=mascota),
        'titulo' : 'Editar Mascota'
    }
    if (request.method == 'POST'):
        form = mascotaForm( request.POST,instance=mascota)
        if (form.is_valid()):
            form.save()
            return redirect("/mascotas")
        else: 
            data['form'] = form
    return render(request, 'crearMascota.html', data)

def editarConsulta(request,id):
    consul = consulta.objects.get(id=id)
    data = {
        'form' : consultaForm(instance=consul),
        'titulo' : 'Editar Consulta'
    }
    if (request.method == 'POST'):
        form = consultaForm( request.POST,instance=consul)
        if (form.is_valid()):
            form.save()
            return redirect("/consultas")
        else: 
            data['form'] = form
    return render(request, 'crearConsulta.html', data)

def editarEstetica(request,id):
    estetica = esteticaVeterinaria.objects.get(id=id)
    data = {
        'form' : esteticaForm(instance=estetica),
        'titulo' : 'Editar Estetica'
    }
    if (request.method == 'POST'):
        form = consultaForm( request.POST,instance=estetica)
        if (form.is_valid()):
            form.save()
            return redirect("/estetica")
        else: 
            data['form'] = form
    return render(request, 'crearEstetica.html', data)

def editarVacuna(request,id):
    vacuna = vacunas.objects.get(id=id)
    data = {
        'form' : vacunaForm(instance=vacuna),
        'titulo' : 'Editar Consulta'
    }
    if (request.method == 'POST'):
        form = consultaForm( request.POST,instance=vacuna)
        if (form.is_valid()):
            form.save()
            return redirect("/vacunas")
        else: 
            data['form'] = form
    return render(request, 'crearVacuna.html', data)

def editarCirugia(request,id):
    cirugia = cirugias.objects.get(id=id)
    data = {
        'form' : cirugiaForm(instance=cirugia),
        'titulo' : 'Editar Cirugia'
    }
    if (request.method == 'POST'):
        form = cirugiaForm( request.POST,instance=cirugia)
        if (form.is_valid()):
            form.save()
            return redirect("/cirugias")
        else: 
            data['form'] = form
    return render(request, 'crearCirugia.html', data)

def eliminarDueno (request,id):
    dueno = ingresoDueno.objects.get(id=id)
    dueno.delete()
    return redirect("/duenos")

def eliminarMascota (request,id):
    mascota = ingresoMascota.objects.get(id=id)
    mascota.delete()
    return redirect("/mascotas")

def eliminarConsulta (request,id):
    consulti = consulta.objects.get(id=id)
    consulti.delete()
    return redirect("/consultas")

def eliminarEstetica (request,id):
    estetica = esteticaVeterinaria.objects.get(id=id)
    estetica.delete()
    return redirect("/estetica")

def eliminarVacuna (request,id):
    vacuna = vacunas.objects.get(id=id)
    vacuna.delete()
    return redirect("/vacunas")

def eliminarCirugia (request,id):
    cirugia = cirugias.objects.get(id=id)
    cirugia.delete()
    return redirect("/cirugias")