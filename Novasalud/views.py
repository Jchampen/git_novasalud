from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def servicios(request):
    return render(request, "servicios.html")