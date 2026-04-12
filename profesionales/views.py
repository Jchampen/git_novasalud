from django.shortcuts import render, redirect
from .models import Profesional
from .forms import ProfesionalForm
from rest_framework import viewsets
from .serializer import ProfesionalSerializer   

class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer    


def crear_profesional(request):
    if request.method == 'POST':
        formulario = ProfesionalForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return render(request, 'profesionales/formProfesional.html', {
                'formulario': ProfesionalForm(),
                'mensaje': 'Profesional creado correctamente'
            })
    else:
        formulario = ProfesionalForm()

    return render(request, 'profesionales/formProfesional.html', {'formulario': formulario})


def profesionales_list(request):
    get_profesionales = Profesional.objects.all()
    data = {
        'get_profesionales': get_profesionales
    }
    return render(request, 'profesionales/profesionalesList.html', data)

def _procesar_edicion_profesional(request, id):
    profesional = Profesional.objects.get(id=id)
    if request.method == 'POST':
        formulario = ProfesionalForm(request.POST, request.FILES, instance=profesional)
        if formulario.is_valid():
            formulario.save()
            return redirect('profesionales_list')
    else:
        formulario = ProfesionalForm(instance=profesional)
    return render(request, 'profesionales/editarProfesional.html', {
        'formulario': formulario,
        'profesional': profesional,
    })


def editar_profesional(request, id):
    return _procesar_edicion_profesional(request, id)


def actualizar_profesional(request, id):
    return _procesar_edicion_profesional(request, id)

def eliminar_profesional(request, id):
    profesional = Profesional.objects.get(id=id)
    if request.method == 'POST':
        profesional.delete()
        return redirect('profesionales_list')
    return render(request, 'profesionales/eliminarProfesional.html', {'profesional': profesional})