from django.urls import path
from . import views

app_name = 'cliente'

urlpatterns = [
    path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
    path('clientes/novo/', views.ClienteCreateView.as_view(), name='cliente_create'),
    path('vendas/nova/', views.VendaClienteCreateView.as_view(), name='venda_create'),
]
