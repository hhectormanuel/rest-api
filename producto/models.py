from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60)
    imagen = models.CharField(max_length=100)


