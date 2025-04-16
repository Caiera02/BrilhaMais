from django.db import models

class Representantes(models.Model):
    nome = models.CharField(max_length=60)
    rg = models.CharField(max_length=20)
    cpf= models.CharField(max_length=20)
    telefone = models.CharField(max_length=20)
    telefone_2 = models.CharField(max_length=20, blank= True, null=True)
    instagram= models.CharField(max_length=30)
    ativo=models.BooleanField(default=True,verbose_name= 'ATIVO')
    inativo=models.BooleanField(verbose_name= 'INATIVO')
    data_criacao= models.DateField(auto_now_add=True,verbose_name= 'Data do cadastro')

    class Meta:
        verbose_name = 'Consultora'

