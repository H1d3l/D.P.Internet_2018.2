from django.forms import *
from core.models import *

class CadastroServicoForm(ModelForm):
    class Meta:
        model = Servico
        fields = '__all__'

class CadastroComboServicoForm(ModelForm):
    class Meta:
        model = ComboServico
        fields = '__all__'


class CadastroCategoriaClienteForm(ModelForm):
    class Meta:
        model = CategoriaCliente
        fields = '__all__'


class CadastroClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'


class CadastroFuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'

class CadastroDiaristaForm(ModelForm):
    class Meta:
        model = Diarista
        fields = '__all__'


class CriarContratoForm(ModelForm):
    class Meta:
        model = Contrato
        fields = '__all__'