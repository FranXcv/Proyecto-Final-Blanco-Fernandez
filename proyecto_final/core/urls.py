from django.contrib import admin
from django.urls import path, include 
from core.views import inicio, mostrar_futbol, editar_futbol, eliminar_futbol, agregar_futbol
urlpatterns = [
    path("", inicio, name="index"),
    path("mostrar_futbol/", mostrar_futbol, name="mostrar_futbol"),
    path("agregar_futbol/", agregar_futbol, name="agregar_futbol"),
    path("editar_futbol/", editar_futbol, name="editar_futbol"),
    path("eliminar_futbol/", eliminar_futbol, name="eliminar_futbol"),
]