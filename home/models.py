from sqlite3 import Timestamp
from django.db import models

# Create your models here.
class equipos(models.Model):
    nombre_equipo = models.CharField(max_length=256)
    categoria = models.CharField(max_length=256)
    estado =  models.CharField(max_length=256)
    director_tecnico = models.CharField(max_length=256)
   

    def __str__(self):
        return self .nombre_equipo + "   " + "-" + "   " + self.categoria
  

class estadios(models.Model):
    nombre_estadio = models.CharField(max_length=256)
    estado =  models.CharField(max_length=256)

    def __str__(self):
        return self .nombre_estadio 
   

class jugadores(models.Model):
    fullname = models.CharField(max_length=256)
    fecha_de_nacimento = models.DateField()
    estado =  models.CharField(max_length=256)
    equipo = models.CharField(max_length=256)

    def __str__(self):
        return self .fullname +  "   " + "-" +  "   " + self.equipo 
