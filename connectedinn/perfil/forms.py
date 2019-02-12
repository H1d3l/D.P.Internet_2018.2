from django import forms
from django.forms import ModelForm
from perfil.models import Justificativa,Perfil, Conversa

class PesquisaUsuariosForm(forms.Form):
    nome = forms.CharField(label='Pesquisar amigo',max_length=100,required=True)

class JustificativaDesativarContaForm(ModelForm):
    class Meta:
        model = Justificativa
        fields =  ["justificativa"]

class UploadFotoPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']


