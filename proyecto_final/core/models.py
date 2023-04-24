from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Futbol(models.Model):
    nombre = models.CharField(max_length=20)
    nro_equipos = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.nro_equipos}"
    

class Arbitros(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    edad = models.IntegerField()
    rol = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido} - {self.edad} - {self.rol}"
    

class Mensaje(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f'{self.autor} - {self.fecha}'
    

    
