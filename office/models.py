from django.db import models

# Create your models here.


class Paquetes(models.Model):
    numeroPaquete = models.CharField(max_length=10, null=False, blank=False)
    nombrePaquete = models.CharField(max_length=200, null=False, blank=False)
    costoPaquete = models.CharField(max_length=100, null=False, blank=False)
    descripcionPaquete = models.CharField(max_length=250, null=False, blank=False)

    class Meta:
        ordering = ['id']