from django.db import models
from vendedoras.models import Produtos

# Create your models here.
class Cliente (models.Model):
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome

class Vendas (models.Model):
    nome =models.ForeignKey(Cliente,on_delete=models.CASCADE, related_name='clinte', verbose_name='Cliente')
    produto = models.ForeignKey(Produtos,on_delete=models.CASCADE, related_name='clinte',verbose_name='Peças')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    pago = models.BooleanField()
    n_pago = models.BooleanField()
    data_compra = models.DateField(auto_now_add=True,verbose_name='Comprado em ')
    data_atualizacao = models.DateField(auto_now=True,verbose_name='Atulizado em ')
