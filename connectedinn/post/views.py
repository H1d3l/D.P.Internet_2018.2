from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect
from post.forms import *
from django.core.paginator import Paginator

def get_perfil_logado(request):
    return request.user.perfil

@login_required
def list_post(request):
    perfil_logado = get_perfil_logado(request)
    postagens_list = Postagem.objects.filter(Q(author=perfil_logado) | Q(author_id__in=perfil_logado.contatos.all()))\
        .order_by('-published_date')
    paginator = Paginator(postagens_list,5)
    page = request.GET.get('page')
    postagens = paginator.get_page(page)
    return render(request,'index.html',{'postagens':postagens,'perfil_logado':get_perfil_logado(request)})

@login_required
def create_post(request):

    if request.method ==  'POST' and request.FILES:
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            texto = form.cleaned_data['text']
            imagem = request.FILES['imagem']
            temp = Postagem(text=texto,imagem=imagem,author=request.user.perfil)
            temp.save()
            return redirect('index')
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            texto = form.cleaned_data['text']
            if not texto :
                messages.warning(request,"Preencha os campos ")
            else:
                temp = Postagem(text=texto,author=request.user.perfil)
                temp.save()
            return redirect('index')


    else:
        return redirect('index')
def excluir_postagem(request,postagem_id):
    postagem = Postagem.objects.get(id = postagem_id)
    postagem.excluir_postagem()
    messages.success(request,"Postagem excluida com sucesso")
    return redirect('index')