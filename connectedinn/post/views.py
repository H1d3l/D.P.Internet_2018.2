from django.contrib.auth.decorators import login_required
from django.db.models import Q

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

    postagens = Postagem.objects.exclude(author_id__in=perfil_logado.bloqueado.all())\
        .filter(Q(author=perfil_logado) | Q(author_id__in=perfil_logado.contatos.all()))\
        .order_by('-published_date')
    return render(request,'postagem/index_postagem.html',{'postagens':postagens,'perfil_logado':get_perfil_logado(request)})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.author = request.user.perfil
            form.save()
            return redirect('index')
    else:
        form = PostForm()
        return render(request, 'postagem/criar_post.html',{'form':form})

def excluir_postagem(request,postagem_id):
    postagem = Postagem.objects.get(id = postagem_id)
    postagem.excluir_postagem()
    return redirect('index')