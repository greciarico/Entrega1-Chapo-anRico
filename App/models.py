from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length = 8)
    email_usuario = models.EmailField()
    
class Datos_Personales(models.Model):
    nombre = models.CharField(max_length = 10)
    apellido = models.CharField(max_length = 20)
    dni = models.CharField(max_length = 8)
    edad = models.IntegerField()
    nacionalidad = models.CharField(max_length = 20)

class Lugar_de_destino(models.Model):
    pais_latinoamericano = models.CharField(max_length = 30)
    ciudad = models.CharField(max_length = 30)
    fecha_de_viaje = models.DateTimeField()
