from django.contrib import admin
from .models import Paquetes

# Register your models here.

@admin.register(Paquetes)
class PaquetesAdmin(admin.ModelAdmin):
    list_display = ("numeroPaquete", "nombrePaquete","costoPaquete", "descripcionPaquete")