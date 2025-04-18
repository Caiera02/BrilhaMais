from django.contrib import admin
from .models import Representantes,Produtos,Produto,Maleta

@admin.register(Representantes)
class RepresentantesAdmin(admin.ModelAdmin):
    list_display= ('nome','cpf','telefone','rua','cep','bairro','numero','cidade','ativo','inativo',)

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 4  # permite inserir até 100 produtos direto

@admin.register(Maleta)
class MaletaAdmin(admin.ModelAdmin):
    inlines = [ProdutoInline]
    list_display = ['nome','consultora','data_criacao', 'valor_total']

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['nome']
    

    
