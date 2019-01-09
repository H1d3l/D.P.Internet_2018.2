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
    postagens = Postagem.objects.filter(Q(author=perfil_logado) | Q(author_id__in=perfil_logado.contatos.all()))\
        .order_by('-published_date')
    return render(request,'index.html',{'postagens':postagens,'perfil_logado':get_perfil_logado(request)})

@login_required
def create_post(request):
    form = PostForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            dados_form = form.cleaned_data
            temp = Postagem()
            temp.author = request.user.perfil
            temp.text = dados_form['text']
            temp.save()
            return redirect('index')
    else:
        return redirect('index')

def excluir_postagem(request,postagem_id):
    postagem = Postagem.objects.get(id = postagem_id)
    postagem.excluir_postagem()
    return redirect('index')