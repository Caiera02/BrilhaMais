from django.contrib import admin
from django.contrib.admin import DateFieldListFilter
from datetime import date
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from vendedoras.models import Representantes,Produto,Maleta,Produtos

class ProdutoInline(admin.TabularInline):
    model = Produto
    extra = 4  # permite inserir até 100 produtos direto

@admin.register(Maleta)
class MaletaAdmin(admin.ModelAdmin):
    inlines = [ProdutoInline]
    list_display = ['consultora','nome','data_criacao','valor_total_formatado','comissaoVendedora','atualizacao']
    search_fields = ['representantes__cpf']
    
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)

    #     # Se o usuário não estiver filtrando manualmente por data,
    #     # mostra apenas os registros de hoje
    #     if 'data_criacao__gte' not in request.GET and 'data_criacao__exact' not in request.GET:
    #         return qs.filter(data_criacao=date.today())
    #     return qs

@admin.register(Representantes)
class RepresentantesAdmin(admin.ModelAdmin):
    list_display= ('nome','cpf','telefone','rua','cep','bairro','numero','cidade','ativo','inativo',)

class ProdutoResource(resources.ModelResource):
    maleta = fields.Field(
        column_name='maleta',
        attribute='maleta',
        widget=ForeignKeyWidget(Maleta, 'nome')  # usar nome do lote
    )

    tipos = fields.Field(
        column_name='tipos',
        attribute='tipos',
        widget=ForeignKeyWidget(Produtos, 'nome')  # Exibe nome da peça
    )

    class Meta:
        model = Produto
        fields = ('maleta', 'tipos', 'valor')  # apenas os campos da planilha
        import_id_fields = []  # <-- ESSENCIAL para evitar erro com 'id'
        skip_unchanged = True
        report_skipped = True

@admin.register(Produto)
class ProdutosAdmin(ImportExportModelAdmin):
    resource_class = ProdutoResource
    list_display = ['maleta','tipos', 'valor']
    list_filter = [
        ('maleta__data_criacao', DateFieldListFilter),
    ]

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['nome']

    

    
