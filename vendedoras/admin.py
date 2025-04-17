from django.contrib import admin
from .models import Representantes

@admin.register(Representantes)
class RepresentantesAdmin(admin.ModelAdmin):
    list_display= ('nome','cpf','telefone','rua','cep','bairro','numero','cidade','ativo','inativo',)

    
