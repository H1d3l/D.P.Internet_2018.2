from django.shortcuts import render,redirect
from core.models import *
from core.forms import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def listaServico(request):
    return render(request, 'listaservico.html', {'servicos': Servico.objects.all(),'combos':ComboServico.objects.all()})

def listCategoriaCliente(request):
    return render(request,'listaCategoriaCliente.html',{'categoria':CategoriaCliente.objects.all()})

def listClientes(request):
    return render(request, 'listaCliente.html',{'clientes':Cliente.objects.all()})

def listFuncionario(request):
    return render(request, 'listaFuncionario.html',{'funcionarios':Funcionario.objects.all()})

def listDiarista(request):
    return render(request, 'listaDiarista.html',{'diaristas':Diarista.objects.all()})

def cadastroServico(request):
    if request.method == 'POST':
        form = CadastroServicoForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaServico')
    else:
        form = CadastroServicoForm()
        return render(request, 'add_servico.html', {'form':form})


def cadastroComboServico(request):
    if request.method == 'POST':
        form = CadastroComboServicoForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaServico')
    else:
        form = CadastroComboServicoForm()
        return render(request, 'add_servico.html', {'form': form})




def cadastroCategoriaCliente(request):
    if request.method == 'POST':
        form = CadastroCategoriaClienteForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('index')
    else:
        form = CadastroCategoriaClienteForm()
        return render(request,'cadastro_categoria_cliente.html',{'form':form})


def cadastroCliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            model_instace = form.save()
            return redirect('index')

    else:
        form = CadastroClienteForm()
        return render(request,'cadastro_cliente.html',{'form':form})




def cadastroFuncionario(request):
    if request.method == 'POST':
        form = CadastroFuncionarioForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('index')
    else:
        form = CadastroFuncionarioForm()
        return render(request, 'add_funcionario.html', {'form': form})

def cadastroDiarista(request):
    if request.method == 'POST':
        form = CadastroDiaristaForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('index')
    else:
        form = CadastroDiaristaForm()
        return render(request, 'add_diarista.html', {'form':form})


def criarContrato(request):
    if request.method == 'POST':
        form = CriarContratoForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('index')
    else:
        form = CriarContratoForm()
        return render(request, 'criar_contrato.html', {'form':form})