from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect,HttpResponse
from post.models import *
from post.forms import *
from perfil.models import *
# Create your views here.

def get_perfil_logado(request):
    return request.user.perfil

@login_required
def list_post(request):
    perfil_logado = get_perfil_logado(request)
    postagens_amigos = Postagem.objects.filter(author_id__in=perfil_logado.contatos.all()).order_by('-published_date')
    minhas_postagens = Postagem.objects.filter(author=perfil_logado).order_by('-published_date')
    return render(request,'postagem/index_postagem.html',{'postagens_amigos':postagens_amigos,
                                                          'minhas_postagens':minhas_postagens})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'postagem/criar_post.html',{'form':form})
