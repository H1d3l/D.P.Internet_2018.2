from django.db import models
from core.utils import testField
# Create your models here.

class CategoriaCliente(models.Model):
    nome = models.CharField(max_length=60,null=False)
    desconto = models.FloatField(default=0)

    def __str__(self):
        return self.nome

class Cliente(models.Model):
    nome = models.CharField(max_length=60,null=False)
    telefone = models.CharField(max_length=20,null=False)
    categoria = models.ForeignKey(CategoriaCliente,on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=60,null=False)
    endereco = models.CharField(max_length=100,null=False)
    telefone = models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=60,null=False)
    valor = models.FloatField(null=False)

    def __str__(self):
        return self.nome

class ComboServico(models.Model):
    nome = models.CharField(max_length=100,null=False)
    servico = models.ManyToManyField(Servico)
    valor = models.FloatField(default=0)


class Diarista(models.Model):
    nome = models.CharField(max_length=60,null=False)
    endereco = models.CharField(max_length=100,null=False)
    telefone = models.CharField(max_length=20,null=False)
    servico = models.ManyToManyField(Servico)

    def __str__(self):
        return self.nome

class Contrato(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    servico = models.ManyToManyField(Servico, related_name="servicos")
    diarista = models.ForeignKey(Diarista,on_delete=models.CASCADE)

    def getSevicos(self):
        return self.servico.all()

    def __str__(self):
        return self.cliente.nome

