from django.db import models
from django.utils import timezone
from perfil.models import *


# Create your models here.


class Postagem(models.Model):
    author = models.ForeignKey(Perfil,on_delete=models.CASCADE,default=None)
    title = models.CharField(max_length=200,null=False)
    text = models.TextField(null=False)
    published_date = models.DateTimeField(blank=True,null=True,default=timezone.now)

    def __str__(self):
        return self.title


    def excluir_postagem(self):
        self.delete()



