from django.forms import *
from core.models import *
class CadastroServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields =    ['nome','valor']