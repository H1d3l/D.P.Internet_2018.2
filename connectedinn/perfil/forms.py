from django import forms

class PesquisaUsuariosForm(forms.Form):
    nome = forms.CharField(label='Pesquisar amigo',max_length=100,required=True)

