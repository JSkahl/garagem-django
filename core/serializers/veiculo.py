from rest_framework.serializers import ModelSerializer

from core.models import Veiculo

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"

class VeiculoDetailSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = "__all__"
        depth = 1