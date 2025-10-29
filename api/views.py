from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated  # 1. Importa esto
from .models import Tarea
from .serializers import TareaSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]  # 2. Añade esta línea