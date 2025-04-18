from django.db import models

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

    class Meta:
        verbose_name = 'Consultora'

class Maleta(models.Model):
    nome = models.CharField(max_length=50, unique=True, verbose_name='Maleta')
    consultora = models.ForeignKey(
        Representantes, on_delete=models.CASCADE, related_name='itens', verbose_name='Consultora')
    data_criacao = models.DateField(auto_now_add=True)

class Produtos(models.Model):
    nome = models.CharField(max_length=20,verbose_name='Peças')

class Produto(models.Model):
    tipos = models.ForeignKey(Produtos,on_delete=models.CASCADE,related_name='produtos')
    maleta = models.ForeignKey(
        Maleta, on_delete=models.CASCADE, related_name='produtos')
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f"{self.produto} - R$ {self.valor}"