from django.shortcuts import render, redirect
from core.models import Futbol, Arbitros, Mensaje
from core.forms import FutbolForm, UserRegisterForm, ArbitrosForm, MensajeForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .forms import SignUpForm
from django.shortcuts import render, redirect


# Create your views here.
def inicio(request):
    return render(request, "core/base.html")

def FormularioFutbol(request):
    futbol = Futbol.objects.all()
    return render(request, "core/FormularioFutbol.html",{"futbol": futbol})

def agregar_futbol(request):
    if request.method == "POST": 
        futbol_form = FutbolForm(request.POST)
        if futbol_form.is_valid():
            data = futbol_form.cleaned_data
            futbol = Futbol(nombre=data["nombre"], nro_equipos=data["integrantes_equipo"])
            futbol.save()
            return render(request, "core/base.html")
    futbol_form = FutbolForm()    
    return render(request, "core/agregar_futbol.html", {"form": futbol_form})

def editar_futbol(request, id_futbol):
    futbol = Futbol.objects.get(id=id_futbol)
    if request.method == "POST":
        futbol_form = FutbolForm(request.POST)
        if futbol_form.is_valid():
            data = futbol_form.cleaned_data
            futbol.nombre = data["nombre"]
            futbol.nro_equipos = data["Integrantes_del_equipo"]
            futbol.save()
            return render(request, "core/index.html")
    return render(request, "core/editar_futbol.html")

def eliminar_futbol(request, id_futbol):

    futbol = Futbol.objects.get(id=id_futbol)
    name = futbol.nombre
    futbol.delete() 
    return render(request, "core/eliminar_futbol.html", {"nombre_eliminado": name})

def leerFutbol(request):
    futbol = Futbol.objects.all()
    contexto = {"futbol":futbol}
    return render(request, "core/leerfutbol.html", contexto )



def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contraseña)

            if user is not None:
                login(request,user)

                return render(request,"core/base.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request,"core/base.html",{"mensaje":"Datos incorrectos"})
        else:
                return render(request,"core/base.html",{"mensaje":"Formulario erroneo"})
        
    form = AuthenticationForm()
    return render(request,"core/login.html",{'form':form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"core/base.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request,"core/register.html",{"form":form})


def home(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def FormularioArbitros(request):
    arbitro = Arbitros.objects.all()
    return render(request, "core/ArbitrosFormulario.html",{"arbitro": arbitro})

def agregar_arbitro(request):
    if request.method == "POST": 
        arbitro_form = ArbitrosForm(request.POST)
        if arbitro_form.is_valid():
            data = arbitro_form.cleaned_data
            arbitro = Arbitros(nombre=data["nombre"],apellido=data["apellido"],edad=data["edad"],rol=data["rol"])
            arbitro.save()
            return render(request, "core/base.html")
        arbitro_form = ArbitrosForm()
        return render(request, "core/agregar_arbitros.html", {"form": arbitro_form})

def editar_arbitro(request, id_arbitro):
    arbitro = Arbitros.objects.get(id=id_arbitro)
    if request.method == "POST":
        arbitro_form = ArbitrosForm(request.POST)
        if arbitro_form.is_valid():
            data = arbitro_form.cleaned_data
            arbitro_form.nombre = data["nombre"]
            arbitro_form.apellido = data["apellido"]
            arbitro_form.edad = data["edad"]
            arbitro_form.rol = data["rol"]
            arbitro.save()
            return render(request, "core/index.html")
    return render(request, "core/editar_arbitro.html")

def eliminar_arbitro(request, id_arbitro):

    arbitro = Arbitros.objects.get(id=id_arbitro)
    nombre = arbitro.nombre
    apellido = arbitro.apellido
    arbitro.delete() 
    return render(request, "core/eliminar_arbitro.html", {"nombre_eliminado": nombre + apellido})

def leerArbitro(request):
    arbitro = Arbitros.objects.all()
    contexto = {"arbitro":arbitro}
    return render(request, "core/leerarbitros.html", contexto )

def mensajes(request):
    mensajes = Mensaje.objects.all().order_by('-fecha')
    form = MensajeForm()

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.save()
            form = MensajeForm()

    return render(request, "core/mensajes.html", {'mensajes': mensajes, 'form': form}) 
#----------------------------------------------------------------------------------------------------------------------------

