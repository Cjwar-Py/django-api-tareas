from django.contrib import admin
from .models import Tarea  # Importa tu modelo

# Registra el modelo Tarea en el admin
admin.site.register(Tarea)