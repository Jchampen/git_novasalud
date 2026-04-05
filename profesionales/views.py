from django.shortcuts import render

# Create your views here.
def profesionaleslist(request):
    return render(request, 'profesionales/profesionaleslist.html')