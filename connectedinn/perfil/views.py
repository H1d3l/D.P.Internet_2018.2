from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from perfil.forms import *
from django.urls import reverse
from post.models import *
from django.db.models import Q
from django.core.paginator import Paginator
from django.db import transaction
from rest_framework import generics
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from perfil.serializers import *


@login_required
def index(request):
    if request.user.perfil.ativo == True:
        perfil_logado = get_perfil_logado(request)
        postagens_list = Postagem.objects.filter(Q(author=perfil_logado) | Q(author_id__in=perfil_logado.contatos.all()))\
            .order_by('-published_date')
        paginator = Paginator(postagens_list, 10)
        page = request.GET.get('page')
        postagens = paginator.get_page(page)
        comentarios = Comentario.objects.all()
        return render(request, 'index.html', {'perfis': Perfil.objects.all(),
                                              'perfil_logado': get_perfil_logado(request),'postagens':postagens,
                                              'comentarios':comentarios})
    else:
        return render(request,'ativar_perfil.html')




@login_required
def meu_perfil(request):
    perfil_logado = get_perfil_logado(request)
    if perfil_logado.ativo == True:
        postagens = Postagem.objects.filter(author=perfil_logado).order_by('-published_date')
        contatos = perfil_logado.contatos.all()
        contatos_bloqueados = perfil_logado.contatos_bloqueados.all()
        return render(request, 'minha_timeline.html', {'perfil':perfil_logado,'postagens':postagens,
                                                            'contatos':contatos,'contatos_bloqueados':contatos_bloqueados})
    else:
        return HttpResponse("nao")


@login_required
def exibir_perfil(request, perfil_id):
    perfil = Perfil.objects.get(id=perfil_id)
    postagens = Postagem.objects.filter(author=perfil).order_by('-published_date')
    return render(request, 'perfil.html',
                  {'perfil': perfil,
                   'perfil_logado': get_perfil_logado(request),'postagens':postagens})


@login_required
@transaction.atomic
def convidar(request, perfil_id):
    perfil_a_convidar = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    if(perfil_logado.pode_convidar(perfil_a_convidar)):
        perfil_logado.convidar(perfil_a_convidar)
    return redirect('index')

@login_required
def get_perfil_logado(request):
    return  request.user.perfil

@login_required
@transaction.atomic
def aceitar(request, convite_id):
    convite = Convite.objects.get(id=convite_id)
    convite.aceitar()
    return redirect('index')

@login_required
@transaction.atomic
def recusar(request,convite_id):
    convite = Convite.objects.get(id = convite_id)
    convite.recusar()
    return redirect('index')

@login_required
def cancelar_solicitacao(request,convite_id):
    convite = Convite.objects.get(id = convite_id)
    convite.cancelar_solicitacao()
    return redirect('index')


@login_required
@transaction.atomic
def desfazer_amizade(request,perfil_id):
    amigo = Perfil.objects.get(id = perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.desfazer_amizade(amigo)
    return redirect('index')

@login_required
@transaction.atomic
def bloquear(request,perfil_id):
    amigo = Perfil.objects.get(id = perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.bloquear_contato(amigo)
    return redirect('meu_perfil')

@login_required
@transaction.atomic
def desbloquear(request,perfil_id):
    amigo = Perfil.objects.get(id=perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.desbloquear_contato(amigo)
    return redirect('meu_perfil')


@login_required
@transaction.atomic
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
            filtro = form.cleaned_data['nome']
            return HttpResponseRedirect(reverse('listaFiltro', args=(filtro,)))
    else:
        redirect('index')

@login_required
def resultado_pesquisa_user(request,filtro):
    perfil_logado = get_perfil_logado(request)
    filtro = Perfil.objects.filter(nome=filtro)
    contatos = perfil_logado.contatos.all()
    return render(request, 'resultado_pesquisa_user.html', {'usuarios':filtro,
                                                                'perfil_logado': get_perfil_logado(request),
                                                                   'contatos':contatos})
@login_required
@transaction.atomic
def promover_super_user(request,usuario_id):
    perfil_logado = get_perfil_logado(request)
    if (perfil_logado.usuario.is_superuser):
        usuario = Perfil.objects.get(id=usuario_id)
        usuario.usuario.is_superuser = True
        usuario.usuario.save()
    else:
        return HttpResponse("Você não é um super usuario")
    return redirect('index')

@login_required
@transaction.atomic
def despromover_super_user(request,usuario_id):
    perfil_logado = get_perfil_logado(request)
    if (perfil_logado.usuario.is_superuser):
        usuario = Perfil.objects.get(id=usuario_id)
        usuario.usuario.is_superuser = False
        usuario.usuario.save()
    else:
        return HttpResponse("Você não é um super usuario")
    return redirect('index')

@login_required
@transaction.atomic
def desativar_perfil(request):
    form = JustificativaDesativarContaForm(request.POST)
    perfil_logado = get_perfil_logado(request)

    if request.method == 'POST':
        if form.is_valid():
            perfil_logado.desativar_perfil()
            model_instance = form.save(commit=False)
            model_instance.perfil = request.user.perfil
            model_instance.save()
            perfil_logado.save()
            return redirect('login')
    else:
        form = JustificativaDesativarContaForm()
    return render(request, 'desabilitarconta.html',{'form':form})



@login_required
@transaction.atomic
def ativar_perfil(request):
    perfil = get_perfil_logado(request)
    perfil.ativar_perfil()
    perfil.save()
    return redirect("login")



@login_required
@transaction.atomic
def uploadfotoperfil(request):
    if request.method == "POST":
        form = UploadFotoPerfilForm(request.POST,request.FILES,instance= request.user.perfil)
        if form.is_valid():
            form.save()
            messages.success(request,"Foto atualizada")
            return redirect('meu_perfil')
    else:
        form = UploadFotoPerfilForm()
    return render(request,"uploadfotoperfil.html",{'form':form})



@api_view(['GET'])
def pesquisar_perfil(request,nome):
    try:
        pesquisa = Perfil.objects.filter(nome=nome)
    except Perfil.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        perfil_serializers = PerfilSerializer(pesquisa,many=True)
        return Response(perfil_serializers.data)
