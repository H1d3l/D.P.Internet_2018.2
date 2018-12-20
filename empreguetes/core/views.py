from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from core.models import *
from core.forms import *


# Create your views here.
def index(request):
    return render(request, 'index.html')


def listaServico(request):
    return render(request, 'listaservico.html',
                  {'servicos': Servico.objects.all(), 'combos': ComboServico.objects.all()})


def listCategoriaCliente(request):
    return render(request, 'listaCategoriaCliente.html', {'categoria': CategoriaCliente.objects.all()})


def listClientes(request):
    return render(request, 'listaCliente.html', {'clientes': Cliente.objects.all()})


def listFuncionario(request):
    return render(request, 'listaFuncionario.html', {'funcionarios': Funcionario.objects.all()})


def listDiarista(request):
    return render(request, 'listaDiarista.html', {'diaristas': Diarista.objects.all()})


def listContrato(request):
    return render(request, 'listaContrato.html', {'contratos': Contrato.objects.all()})


def cadastroServico(request):
    if request.method == 'POST':
        form = CadastroServicoForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaServico')
    else:
        form = CadastroServicoForm()
        return render(request, 'add_servico.html', {'form': form})


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
        return render(request, 'cadastro_categoria_cliente.html', {'form': form})


def cadastroCliente(request):
    if request.method == 'POST':
        form = CadastroClienteForm(request.POST)
        if form.is_valid():
            model_instace = form.save()
            return redirect('index')

    else:
        form = CadastroClienteForm()
        return render(request, 'cadastro_cliente.html', {'form': form})


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
        return render(request, 'add_diarista.html', {'form': form})


def criarContrato(request):
    if request.method == 'POST':
        form = CriarContratoForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('index')
    else:
        form = CriarContratoForm()
        return render(request, 'criar_contrato.html', {'form': form})


def editarServico(request, pk):
    editserv = get_object_or_404(Servico, pk=pk)

    if request.method == "POST":
        form = CadastroServicoForm(request.POST, instance=editserv)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaServico')
    else:
        form = CadastroServicoForm(instance=editserv)
        return render(request, 'add_servico.html', {'form': form})


def excluirServico(request, pk):
    excluiserv = get_object_or_404(Servico, pk=pk)
    excluiserv.delete()
    return redirect('listaServico')

def resultadoPesquisa(request,filtro):
    listaFiltro = Diarista.objects.filter(nome__contains=filtro)
    return render(request, "pesquisaDiaristaLista.html",{'diaristas': listaFiltro})

def pesquisarDiarista(request):
    # pesquisa = get_object_or_404(Diarista.objects.all())
    form = PesquisaForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            filtro = form.cleaned_data['item']
            return HttpResponseRedirect(reverse('listaFiltro', args=(filtro,)))
    return render(request, 'pesquisa.html', {'form': form})



def editarCliente(request, pk):
    editcli = get_object_or_404(Cliente, pk=pk)

    if request.method == "POST":
        form = CadastroClienteForm(request.POST, instance=editcli)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaClientes')
    else:
        form = CadastroClienteForm(instance=editcli)
        return render(request, 'cadastro_cliente.html', {'form': form})


def excluirCliente(request, pk):
    excluicli = get_object_or_404(Cliente, pk=pk)
    excluicli.delete()
    return redirect('listaClientes')


def editarDiarista(request, pk):
    editdia = get_object_or_404(Diarista, pk=pk)

    if request.method == "POST":
        form = CadastroDiaristaForm(request.POST, instance=editdia)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaDiarista')
    else:
        form = CadastroDiaristaForm(instance=editdia)
        return render(request, 'add_diarista.html', {'form': form})


def excluirDiarista(request, pk):
    excluidia = get_object_or_404(Diarista, pk=pk)
    excluidia.delete()
    return redirect('listaClientes')

def editarFuncionario(request, pk):
    editfunc = get_object_or_404(Funcionario, pk=pk)

    if request.method == "POST":
        form = CadastroFuncionarioForm(request.POST, instance=editfunc)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaFuncionario')
        if Funcionario.nome == Funcionario.nome:
            raise forms.ValidationError("Nome já presente no banco")
    else:
        form = CadastroFuncionarioForm(instance=editfunc)
        return render(request, 'add_funcionario.html', {'form': form})

def excluirFuncionario(request,pk):
    excluifunc = get_object_or_404(Funcionario, pk=pk)
    excluifunc.delete()
    return redirect('listaFuncionario')



def editarCategoria(request, pk):
    editcat = get_object_or_404(CategoriaCliente, pk=pk)

    if request.method == "POST":
        form = CadastroCategoriaClienteForm(request.POST, instance=editcat)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaCategoriaCliente')

    else:
        form = CadastroCategoriaClienteForm(instance=editcat)
        return render(request, 'cadastro_categoria_cliente.html', {'form': form})

def excluirCategoria(request,pk):
    excluicat = get_object_or_404(CategoriaCliente, pk=pk)
    excluicat.delete()
    return redirect('listaCategoriaCliente')