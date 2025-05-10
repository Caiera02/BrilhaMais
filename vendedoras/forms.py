from django import forms
from django.core.exceptions import ValidationError
from vendedoras.models import Representantes

class RepresentantesModelForm(forms.ModelForm):
    telefone= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '11 90200-0300'})
    )
    telefone_2= forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': '11 90200-0300'})
    )
    instagram=forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'instagram.com/seu_perfil'})
    )

    class Meta:
        model= Representantes
        fields = '__all__'