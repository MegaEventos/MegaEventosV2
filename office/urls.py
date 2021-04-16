from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pdf/<int:pk>/', login_required(views.GeneratePDF.as_view()) , name='GeneratePDF'),
    path('editar/<int:clave_id>', views.edit, name="edit"),
    path('eliminar/<int:clave_id>', views.delete, name="delete"),
    path('reciclaje/', views.reciclaje, name="reciclaje"),
    path('restaurar/<int:clave_id>', views.restore, name="restore"),
]