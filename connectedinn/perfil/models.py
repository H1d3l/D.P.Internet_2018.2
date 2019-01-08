from django.db import models
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import request




# Create your models here.


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User,related_name="perfil",on_delete=models.CASCADE)
    contatos_bloqueados = models.ManyToManyField('self',related_name='meus_contatos_bloqueados', symmetrical=False, through="Bloqueio")



    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return self.nome

    def pode_convidar(self,perfil_convidado):
        pode_convidar = False
        if perfil_convidado not in self.contatos.all():
            pode_convidar = True
        return pode_convidar

    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self,convidado = perfil_convidado)
            convite.save()


    def desfazer_amizade(self,perfil_id):
        self.contatos.remove(perfil_id)

    def bloquear_contato(self,perfil):
        bloqueio = Bloqueio(perfil_bloqueador=self,perfil_bloqueado=perfil)
        bloqueio.save()

    def desbloquear_contato(self,perfil):
        print(1111111111111111111111)
        bloqueios = Bloqueio.objects.filter(perfil_bloqueador = self, perfil_bloqueado=perfil).all()
        for b in bloqueios:
            b.delete()


class Convite(models.Model):
    solicitante = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='convites_feitos' )
    convidado = models.ForeignKey(Perfil, on_delete= models.CASCADE, related_name='convites_recebidos')

    def aceitar(self):
        self.solicitante.contatos.add(self.convidado)
        self.convidado.contatos.add(self.solicitante)
        self.delete()

    def recusar(self):
        self.delete()

class Bloqueio(models.Model):
    perfil_bloqueador = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='bloqueador')
    perfil_bloqueado = models.ForeignKey(Perfil,on_delete=models.CASCADE,related_name='bloqueado')



