from django.contrib import admin
from django.urls import path, include 
from core.views import inicio, mostrar_futbol
urlpatterns = [
    path("", inicio, name="index"),
    path("mostrar_futbol", mostrar_futbol, name="futbol"),
]