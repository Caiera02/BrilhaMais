from django.db import models
from vendedoras.models import Produtos,Maleta

class Venda (models.Model):
    produto = models.ForeignKey(Produtos,on_delete=models.CASCADE,related_name='products')
    maleta = models.ForeignKey(Maleta, on_delete=models.CASCADE, related_name='products')
    valor = models.DecimalField(max_digits=8, decimal_places=2)