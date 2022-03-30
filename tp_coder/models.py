from django.db import models

# Create your models here.

class Vendedor(models.Model):
    id_vend = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=20)
    
class Automoviles(models.Model):
    chasis = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    kms = models.IntegerField()
    anio = models.IntegerField()

class Motocicletas(models.Model):
    chasis = models.IntegerField(primary_key=True)
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    kms = models.IntegerField()
    anio = models.IntegerField()
