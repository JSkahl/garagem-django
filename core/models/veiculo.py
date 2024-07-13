from django.db import models

from .modelo import Modelo
from .cor import Cor
from .acessorio import Acessorio

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="modelos")
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name="cores")
    acessorios = models.ManyToManyField(Acessorio, related_name="acessorios")
    ano = models.IntegerField(blank=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return f"{self.modelo} ({self.cor}) - {self.ano}"