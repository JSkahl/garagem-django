from django.contrib import admin

from garagem.models import Marca, Modelo, Acessorio, Cor, Veiculo

admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Veiculo)