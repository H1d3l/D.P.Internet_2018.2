"""connectedinn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from perfil import views as perfilview
from usuario.views import *
from django.contrib.auth import views as auth_views
from post import views as postview
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', perfilview.index, name='index'),
    path('index/<int:postagem_id>',postview.excluir_postagem,name = 'excluir_postagem'),
    path('perfil/<int:perfil_id>/bloquear',perfilview.bloquear,name = 'bloquear'),
    path('perfil/<int:perfil_id>/desbloquear',perfilview.desbloquear,name = 'desbloquear'),
    path('perfil/<int:perfil_id>', perfilview.exibir_perfil, name='exibir'),
    path('perfil/<int:perfil_id>', perfilview.exibir_perfil, name='send_message'),
    path('perfil/minha_timeline',perfilview.meu_perfil,name = 'meu_perfil'),
    path('perfil/minha_timeline/ativar', perfilview.ativar_perfil, name='ativar'),
    path('perfil/minha_timeline/desativar',perfilview.desativar_perfil,name='desativar'),
    path('perfil/minha_timeline/uploadfotoperfil',perfilview.uploadfotoperfil,name = 'uploadfotoperfil'),
    path('perfil/<int:perfil_id>/convidar',perfilview.convidar, name='convidar'),
    path('convite/<int:convite_id>/aceitar',perfilview.aceitar, name='aceitar'),
    path('convite/<int:convite_id>/recusar', perfilview.recusar, name='recusar'),
    path('convite/<int:convite_id>/cancelar_solicitacao', perfilview.cancelar_solicitacao, name='cancelar_solicitacao'),
    path('perfil/<int:perfil_id>/desfazer_amizade', perfilview.desfazer_amizade, name='desfazer'),
    path('registrar/', RegistrarUsuarioView.as_view(), name='registrar'),
    path('login/',auth_views.LoginView.as_view(template_name = 'login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'login.html'),name = 'logout'),
    path('password/',perfilview.alterar_senha,name = 'alterar_senha'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name = 'registration/password_reset_form.html')
         ,name ='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name = 'registration/password_reset_done.html'),
     name ='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'registration/password_reset_confirm.html'),
     name ='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name = 'registration/password_reset_complete.html'),
     name ='password_reset_complete'),
    path('index/',postview.create_post,name = 'criar_post'),
    path('index/<int:postagem_id>/comentario', postview.comentar_postagem, name='comentar_post'),
    path('pesquisa/',perfilview.pesquisar_user,name='pesquisar_user'),
    path('lista-filtro/<filtro>/', perfilview.resultado_pesquisa_user, name='listaFiltro'),
    path('usuarios/<int:usuario_id>/promover',perfilview.promover_super_user,name = 'promover_super_user'),
    path('usuarios/<int:usuario_id>/despromover', perfilview.despromover_super_user, name='despromover_super_user'),
    path('perfil/<str:nome>',perfilview.pesquisar_perfil,name='pesquisar_perfil_api'),
    path('token-auth-api/',obtain_auth_token),
    path('postar-api/',postview.PostarApi.as_view(),name=postview.PostarApi.name)





]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


