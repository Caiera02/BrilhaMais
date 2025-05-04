from django.contrib import admin
from django.urls import path
from vendedoras.views import cadastro_view, maleta_view, home_view
from accounts.views import registro_view, login_view
from contabilidade.views import salvar_vendas,vendas_view

urlpatterns = [
    path('admin/', admin.site.urls,name='admin_1'),
    path('cadastro/new_user',registro_view,name='registro'),
    path('login/',login_view,name='login'),
    path('cadastro/consultora',cadastro_view,name='new_cadastro'),
    path('maleta/',maleta_view,name='produto_list'),
    path('salvar/',salvar_vendas,name='vendas_list'),
    path('maleta/vendas/',vendas_view,name='visualizar_venda'),
    path('',home_view,name='home_list'),
]
