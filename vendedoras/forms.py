from django import forms
from vendedoras.models import Representantes

class RepresentantesModelForm(forms.ModelForm):
    class Meta:
        model= Representantes
        fields = '__all__'
