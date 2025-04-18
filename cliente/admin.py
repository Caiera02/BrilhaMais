from django.contrib import admin
from cliente.models import Cliente,Vendas

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome','telefone']

@admin.register(Vendas)
class VendasAdmin(admin.ModelAdmin):
    list_display= ['nome','valor','pago','n_pago','data_compra']

    

    

    
