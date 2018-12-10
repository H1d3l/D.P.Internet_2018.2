from django.forms import *
from core.models import *
class CadastroServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

class CadastroComboServicoForm(ModelForm):
    class Meta:
        model = ComboServico
        fields = ['nome','servico','valor']