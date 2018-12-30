from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from perfil.models import Perfil, Convite
from django.shortcuts import redirect


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

def recusar(request,convite_id):
    convite = Convite.objects.get(id = convite_id)
    convite.recusar()
    return redirect('index')

def desfazer_amizade(request,perfil_id):
    amigo = Perfil.objects.get(id = perfil_id)
    perfil_logado = get_perfil_logado(request)
    perfil_logado.desfazer_amizade(amigo)
    return redirect('index')