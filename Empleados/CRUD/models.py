from django.db import models

class Empleados(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)


             