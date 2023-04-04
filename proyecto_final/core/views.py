from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, "core/base.html")

def mostrar_futbol(request):
    return render(request, "core/mostrar_futbol.html")