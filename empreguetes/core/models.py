from django.db import models
from core.utils import testField
# Create your models here.

class CategoriaCliente(models.Model):
    nome = models.CharField(max_length=60,null=False)
    desconto = testField.PercentageField()

class Cliente(models.Model):
    nome = models.CharField(max_length=60,null=False)
    telefone = models.CharField(max_length=20,null=False)
    categoria = models.OneToOneField(CategoriaCliente,on_delete=models.CASCADE)


class Funcionario(models.Model):
    nome = models.CharField(max_length=60,null=False)
    endereco = models.CharField(max_length=100,null=False)
    telefone = models.CharField(max_length=20,null=False)

class Servico(models.Model):
    nome = models.CharField(max_length=60,null=False)
    valor = models.FloatField(null=False)

class Diarista(models.Model):
    nome = models.CharField(max_length=60,null=False)
    endereco = models.CharField(max_length=100,null=False)
    telefone = models.CharField(max_length=20,null=False)
    servico = models.ManyToManyField(Servico)

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,null=False)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE,null=False)
    servico = models.ManyToManyField(Servico)
    diarista = models.ForeignKey(Diarista,on_delete=models.CASCADE,null=False)








