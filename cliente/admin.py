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
    list_display= ['nome','valor_formatado','pago','n_pago','data_compra_formatada','data_atualizacao',]
    list_filter = ['pago','n_pago']
    exclude = ['nome',]
    
    def valor_formatado(self,obj):
        return f'R$ {obj.valor}'
    
    def data_compra_formatada(self, obj):
        return obj.data_compra.strftime('%d/%m/%Y')
    data_compra_formatada.short_description = 'Comprado em'
    
    

    

    

    
