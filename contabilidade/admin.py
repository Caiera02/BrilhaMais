from django.contrib import admin
from contabilidade.models import Venda

# Register your models here.
@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display=['produto','maleta','valor','data_venda','data_atualizada']
    
