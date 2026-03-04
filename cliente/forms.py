from django import forms
from .models import Cliente, Vendas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Cliente'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) XXXXX-XXXX'}),
        }

class VendaClienteForm(forms.ModelForm):
    class Meta:
        model = Vendas
        fields = ['nome', 'produto', 'valor', 'pago', 'n_pago']
        widgets = {
            'nome': forms.Select(attrs={'class': 'form-control'}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'n_pago': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
