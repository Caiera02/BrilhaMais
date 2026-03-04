from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Cliente, Vendas
from .forms import ClienteForm, VendaClienteForm

class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    context_object_name = 'clientes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass all sales alongside clients in context, or sales can be gathered directly in template
        # depending on if we just want a flat list. We'll pass a flat list of sales as well.
        context['vendas'] = Vendas.objects.all().order_by('-data_compra')
        return context

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Novo Cliente'
        return context

class VendaClienteCreateView(CreateView):
    model = Vendas
    form_class = VendaClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nova Venda para Cliente'
        return context
