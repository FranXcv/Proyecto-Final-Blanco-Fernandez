from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/base.html")

def mostrar_futbol(request):
    return render(request, "core/mostrar_futbol.html")

def agregar_futbol(request):
    return render(request, "core/agregar_futbol.html")

def editar_futbol(request):
    return render(request, "core/editar_futbol.html")

def eliminar_futbol(request):
    return render(request, "core/eliminar_futbol.html")
