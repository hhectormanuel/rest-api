from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=999)
    marca = models.CharField(max_length=999)
    descripcion = models.CharField(max_length=999)
    imagen = models.CharField(max_length=999)
    precio = models.FloatField()
    stock = models.IntegerField()


