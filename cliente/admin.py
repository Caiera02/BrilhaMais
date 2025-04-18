from django.contrib import admin
from cliente.models import Cliente,Vendas
# from vendedoras.models import Produto


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','telefone']

# class ProdutoInline(admin.TabularInline):
#     model = Produto
#     extra = 4  # permite inserir até 100 produtos direto

@admin.register(Vendas)
class VendasAdmin(admin.ModelAdmin):
    # inlines = [ProdutoInline]
    list_display= ['nome','valor','pago','n_pago','data_compra']

    

    

    
