from rest_framework.viewsets import ModelViewSet

from core.models import categoria
from core.serializers import CategoriaSerializer

class CategoriaViewSet(ModelViewSet):
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer