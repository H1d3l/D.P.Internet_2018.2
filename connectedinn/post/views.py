from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render,redirect
from post.forms import *
from django.core.paginator import Paginator
from django.db import transaction
from rest_framework import generics,permissions
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from post.serializers import *



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
@transaction.atomic
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

@login_required
@transaction.atomic
def excluir_postagem(request,postagem_id):
    postagem = Postagem.objects.get(id = postagem_id)
    postagem.excluir_postagem()
    messages.success(request,"Postagem excluida com sucesso")
    return redirect('index')

def comentar_postagem(request,postagem_id):
    if request.method == 'POST':
        form = ComentarioPostForm(request.POST)
        if form.is_valid():
            comentario = form.cleaned_data['comentario']
            if not comentario :
                messages.warning(request,"Comente algo")
            else:
                postagem = Postagem.objects.get(id=postagem_id)
                comentario = Comentario(postagem=postagem, autor=request.user.perfil,
                                        texto=comentario)
                comentario.save()
        return redirect('index')


"""
@api_view(['POST'])
def postar(request):
    if request.method == 'POST':
        post_serializer = PostSerializers(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save(author=request.user.perfil)
            return Response(post_serializer.data,status=status.HTTP_201_CREATED)
        return Response(post_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

"""


class PostarApi(generics.ListCreateAPIView):
    postagens = Postagem.objects.all()
    serializer_class = PostSerializers
    name='postagemapi'
    permission_classes = (permissions.IsAuthenticated,permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.perfil)

