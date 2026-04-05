from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def servicios(request):
    return render(request, "servicios.html")


def profesionales(request):
    return render(request, "templates/profesionales/profesionaleslist.html")