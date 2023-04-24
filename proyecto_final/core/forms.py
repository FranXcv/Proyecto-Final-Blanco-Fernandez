from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class FutbolForm(forms.Form): 
    nombre = forms.CharField(max_length=20)
    integrantes_equipo = forms.IntegerField()


class ArbitrosForm(forms.Form): 
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    rol = forms.CharField(max_length=20)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= "contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label= "repite la contraseña", widget=forms.PasswordInput)
    
    class meta: 
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Este campo es requerido.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['texto']

