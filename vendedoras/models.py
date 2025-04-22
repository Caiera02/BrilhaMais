from django.db import models
from decimal import Decimal
from django.utils.safestring import mark_safe

class Representantes(models.Model):
    nome = models.CharField(max_length=60)
    rg = models.CharField(max_length=20)
    cpf= models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    telefone_2 = models.CharField(max_length=20, blank= True, null=True)
    instagram= models.CharField(max_length=30)
    data_criacao= models.DateField(auto_now_add=True,verbose_name= 'Data do cadastro')
    rua= models.CharField(max_length=50,blank= True, null=True)
    cep= models.CharField(max_length=20,blank= True, null=True)
    numero = models.IntegerField(blank= True, null=True)
    cidade= models.CharField(max_length=20,blank= True, null=True)
    bairro= models.CharField(max_length=20,blank= True, null=True)
    ativo=models.BooleanField(default=True,verbose_name= 'ATIVO')
    inativo=models.BooleanField(verbose_name= 'INATIVO')

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Consultora'

class Maleta(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name='Mostruario')
    consultora = models.ForeignKey(
        Representantes, on_delete=models.CASCADE, related_name='itens', verbose_name='Consultora')
    data_criacao = models.DateField(auto_now_add=True,verbose_name= 'Data de Saida')
    atualizacao = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    def __str__(self):
        return self.nome
    
    def valor_total(self):
        return self.produtos.aggregate(total=models.Sum('valor'))['total'] or 0
    
    def valor_total_formatado(self):
        total = self.valor_total()
        if total is None:
            total = 0
        return mark_safe(f"R$ {total:,.2f}".replace(",", "X").replace(".", ".").replace("X", "."))

    valor_total_formatado.short_description = "VALOR TOTAL"
    
    def comissaoVendedora(self):
        total = self.valor_total()
        
        if total >=1000:
            porcentagem = Decimal('0.05')
        elif total >=2000:
            porcentagem = Decimal('0.10')
        elif total >=3000:
            porcentagem= Decimal('0.20')
        else:
            porcentagem = Decimal('0.00')#sem comissão
        return round(total * porcentagem, 2)
    
    class Meta:
        verbose_name ='Mostruario'

class Produtos(models.Model):
    nome = models.CharField(max_length=20,verbose_name='Peças')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    tipos = models.ForeignKey(Produtos,on_delete=models.CASCADE,related_name='produtos')
    maleta = models.ForeignKey(
        Maleta, on_delete=models.CASCADE, related_name='produtos')
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    # data_criacao

    def __str__(self):
        return f"{self.tipos} - R$ {self.valor}"