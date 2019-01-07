from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from perfil.models import Perfil, Convite
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from perfil.forms import *
from django.urls import reverse

# Create your views here.
@login_required
def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all(),
                                          'perfil_logado': get_perfil_logado(request)})

@login_required
def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)

    return render(request, 'perfil.html',
                  {'perfil': perfil,
                   'perfil_logado': get_perfil_logado(request)})

@login_required
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

@login_required
def get_perfil_logado(request):
    return  request.user.perfil

@login_required
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')
@login_required
def recusar(request,convite_id):
    convite = Convite.objects.get(id = convite_id)
    convite.recusar()
    return redirect('index')
@login_required
def desfazer_amizade(request,perfil_id):
    amigo = Perfil.objects.get(id = perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.desfazer_amizade(amigo)
    return redirect('index')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('index')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form': form})
@login_required
def pesquisar_user(request):
    form = PesquisaUsuariosForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            filtro = form.cleaned_data['item']
            return HttpResponseRedirect(reverse('listaFiltro', args=(filtro,)))
    return render(request, 'postagem/pesquisa_user.html', {'form': form})

@login_required
def resultado_pesquisa_user(request,filtro):
    filtro = Perfil.objects.filter(nome=filtro)
    return render(request,'postagem/resultado_pesquisa_user.html',{'usuarios':filtro,
                                                                   'perfil_logado': get_perfil_logado(request)})

def super_user(request,usuario_id):
    usuario = Perfil.objects.get(id=usuario_id)
    usuario_is_super = usuario.usuario.is_superuser = True
    usuario.usuario.save()
    return redirect('index')


def lista_user(request):
    perfil_logado = get_perfil_logado(request)
    if perfil_logado.usuario.is_superuser:
        usuarios = Perfil.objects.all()
        return render(request, 'postagem/lista_user.html',{'usuarios':usuarios})
    else:
        return HttpResponse("Você não é um super usuario")

