from django.db import models
from core.utils import testField
# Create your models here.

class CategoriaCliente(models.Model):
    nome = models.CharField(max_length=60,null=False)
    desconto = testField.PercentageField(null=False)

class Cliente(models.Model):
    nome = models.CharField(max_length=60,null=False)
    telefone = models.CharField(max_length=20,null=False)
    categoria = models.OneToOneField(CategoriaCliente,on_delete=models.CASCADE())


class Funcionario(models.Model):
    nome = models.CharField(max_length=60,null=False)
    endereço = models.CharField(max_length=100,null=False)
    telefone = models.CharField(max_length=20,null=False)

class Serviço(models.Model):
    nome = models.CharField(max_length=60,null=False)
    valor = models.FloatField(null=False)

class Solicitação(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE(),null=False)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE(),null=False)
    serviço = models.ManyToManyField(Serviço,null=False)






class Diarista(models.Model):
    nome = models.CharField(max_length=60,null=False)
    endereço = models.CharField(max_length=100,null=False)
    telefone = models.CharField(max_length=20,null=False)