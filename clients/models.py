from django.db import models

# Create your models here.

class Clients(models.Model):
    nombreCliente = models.CharField(max_length=100, null=False, blank=False)
    nombreHomenajeado = models.CharField(max_length=100, null=False, blank=False)
    celular = models.CharField(max_length=20, null=False, blank=False)
    barrioSector = models.CharField(max_length=200, null=False, blank=False)
    direccion = models.CharField(max_length=200, null=False, blank=False)
    fechaEvento = models.CharField(max_length=20, null=False, blank=False)
    horaInicio = models.CharField(max_length=20, null=False, blank=False)
    numeroPaquete = models.CharField(max_length=10, null=False, blank=False)
    cantidadNinos = models.CharField(max_length=100, null=False, blank=False)
    rangoEdad = models.CharField(max_length=100, null=False, blank=False)
    Recycle = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']