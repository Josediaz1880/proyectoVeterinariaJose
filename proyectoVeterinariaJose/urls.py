"""proyectoVeterinariaJose URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from veterinariaAPP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('duenos/',views.viewDuenos, name='duenos'),
    path('mascotas/',views.viewMascotas, name='mascotas'),
    path('consultas/',views.viewConsultas, name='consultas'),
    path('estetica/',views.viewEstetica, name='estetica'),
    path('vacunas/',views.viewVacunas, name='vacunas'),
    path('cirugias/',views.viewCirugias, name='cirugias'),
    path('duenos/agregar/',views.crearDueno, name='agregar'),
    path('duenos/editar/<int:id>',views.editarDueno, name='editar'),
    path('duenos/eliminarDueno/<int:id>',views.eliminarDueno, name='eliminar'),
    path('mascotas/agregarMascota/',views.crearMascota, name='agregarMascotas'),
    path('mascotas/editarMascota/<int:id>',views.editarMascota, name='editarMascota'),
    path ('mascotas/eliminarMascota/<int:id>',views.eliminarMascota,name='eliminarMascota'),
    path('consultas/agregarConsulta/',views.crearConsulta, name='agregarConsulta'),
    path('consultas/eliminarConsulta/<int:id>',views.eliminarConsulta, name='eliminarConsulta'),
    path('consultas/editarConsulta/<int:id>',views.editarConsulta,name='editarConsulta'),
    path('estetica/agregarEstetica/',views.crearEstetica, name='crearEstetica'),
    path('estetica/editarEstetica/<int:id>',views.editarEstetica, name='editarEstetica'),
    path('estetica/eliminarEstetica/<int:id>',views.eliminarEstetica, name='eliminarEstetica'),
    path('vacunas/agregarVacuna/',views.crearVacuna, name='crearVacuna'),
    path('vacunas/eliminarVacuna/<int:id>',views.eliminarVacuna, name='eliminarVacuna'),
    path('vacunas/editarVacuna/<int:id>',views.editarVacuna, name='editarVacuna'),
    path('cirugias/agregarCirugia/',views.crearCirugia, name='agregarCirugia'),
    path('cirugias/eliminarCirugia/<int:id>',views.eliminarCirugia, name='eliminarCirugia'),
    path('cirugias/editarCirugia/<int:id>',views.editarCirugia,name='editarCirugia'),


    
]
