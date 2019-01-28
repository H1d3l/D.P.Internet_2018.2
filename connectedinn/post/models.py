from django.db import models
from django.utils import timezone
from perfil.models import *


# Create your models here.

class Postagem(models.Model):
    author = models.ForeignKey(Perfil,on_delete=models.CASCADE,default=None)
    text = models.TextField(null=False)
    published_date = models.DateTimeField(blank=True,null=True,default=timezone.now)
    imagem = models.ImageField(upload_to= 'postagemimagem',blank=True,null=True)



    def excluir_postagem(self):
        self.delete()



