from rest_framework.viewsets import ModelViewSet

from core.models import Modelo
from core.serializers import ModeloSerializer, ModeloDetailSerializer

class ModeloViewSet(ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ModeloDetailSerializer
        return ModeloSerializer