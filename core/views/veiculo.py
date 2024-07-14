from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import VeiculoSerializer, VeiculoDetailSerializer

class VeiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return VeiculoDetailSerializer
        return VeiculoSerializer