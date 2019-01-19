from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class Perfil(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=20, null= False)
    nome_empresa = models.CharField(max_length=255, null=False)
    contatos = models.ManyToManyField('self')
    usuario = models.OneToOneField(User,related_name="perfil",on_delete=models.CASCADE)
    contatos_bloqueados = models.ManyToManyField('self',related_name='meus_contatos_bloqueados', symmetrical=False, through="Bloqueio")
    ativo = models.BooleanField(default=True)

    @property
    def email(self):
        return self.usuario.email

    def __str__(self):
        return self.nome

    def pode_convidar(self,perfil_convidado):
        convites_recebidos = Convite.objects.filter(solicitante=perfil_convidado, convidado=self)
        convites_enviados = Convite.objects.filter(solicitante=self, convidado=perfil_convidado)


        if perfil_convidado in self.contatos.all():
            return False
        elif perfil_convidado == self:
            return False
        elif self in perfil_convidado.contatos_bloqueados.all():
            return False
        elif convites_enviados:
            return False
        elif convites_recebidos:
            return False
        else:
            return True


    def convidar(self, perfil_convidado):
        if self.pode_convidar(perfil_convidado):
            convite = Convite(solicitante=self,convidado = perfil_convidado)
            convite.save()


    def desfazer_amizade(self,perfil_id):
        self.contatos.remove(perfil_id)

    def pode_bloquear(self,perfil_bloqueado):

        if perfil_bloqueado == self:
            return False
        else:
            return True


    def bloquear_contato(self,perfil_bloqueado):
        if self.pode_bloquear(perfil_bloqueado):
            bloqueio = Bloqueio(perfil_bloqueador=self,perfil_bloqueado=perfil_bloqueado)
            bloqueio.save()
            self.desfazer_amizade(perfil_bloqueado)



    def desbloquear_contato(self,perfil_bloqueado):
        bloqueio = Bloqueio.objects.filter(perfil_bloqueador = self, perfil_bloqueado=perfil_bloqueado)
        bloqueio.delete()


    def ativar_perfil(self):
        self.ativo = True

    def desativar_perfil(self):
        self.ativo = False


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



class Justificativa(models.Model):
    perfil = models.ForeignKey(Perfil,on_delete=models.CASCADE)
    justificativa = models.TextField()