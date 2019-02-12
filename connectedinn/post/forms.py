from django.forms import ModelForm
from post.models import *
from django import forms



class PostForm(forms.Form):
    text = forms.CharField(required=False)
    imagem = forms.ImageField(required=False)

class ComentarioPostForm(forms.Form):
    comentario = forms.CharField(required=True)

