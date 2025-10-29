from django.urls import path, include
from rest_framework.routers import DefaultRouter
# Fíjate que ahora importa TareaViewSet, no ListaTareas
from .views import TareaViewSet

# Crea un router
router = DefaultRouter()
# Registra tu ViewSet
router.register(r'tareas', TareaViewSet, basename='tarea')

# Las URLs de la API ahora son generadas automáticamente por el router
urlpatterns = [
    path('', include(router.urls)),
]