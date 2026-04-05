from django.shortcuts import render
from .models import Profesional

# Create your views here.
def profesionaleslist(request):
    return render(request, 'profesionales/profesionaleslist.html')

def profesionaleslist(request):
    get_profesionales = Profesional.objects.all()
    data={
        'get_profesionales': get_profesionales
    }
    return render(request, 'profesionales/profesionaleslist.html', data)