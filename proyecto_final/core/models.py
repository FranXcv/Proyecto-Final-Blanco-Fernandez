from django.db import models

# Create your models here.
class Futbol(models.Model):
    nombre = models.CharField(max_length=20)
    nro_equipos = models.IntegerField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.nro_equipos}"