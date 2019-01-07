from django import forms

class PesquisaUsuariosForm(forms.Form):
    item = forms.CharField(label='Pesquisar amigo',max_length=100)

