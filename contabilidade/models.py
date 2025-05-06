from django.db import models
from vendedoras.models import Produto,Maleta

class Venda (models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name='vendas')
    maleta = models.ForeignKey(Maleta, on_delete=models.CASCADE, related_name='vendas')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    data_venda = models.DateField(auto_now_add=True,verbose_name='Venda')
    data_atualizada = models.DateField(auto_now=True,verbose_name='Atualizado em')
        
    def __str__(self):
        return f"{self.produto}"