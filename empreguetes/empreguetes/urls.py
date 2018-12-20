"""empreguetes URL Configuration

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
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('servico/', views.listaServico, name='listaServico'),
    path('editarservico/<int:pk>', views.editarServico, name='editarServico'),
    path('excluiservico/<int:pk>', views.excluirServico, name='excluiServico'),
    path('pesquisaDiarista/', views.pesquisarDiarista, name='pesquisaDiarista'),

    path('editarCategoria/<int:pk>', views.editarCategoria, name='editarCategoria'),
    path('excluiCategoria/<int:pk>', views.excluirCategoria, name='excluiCategoria'),

    path('excluicliente/<int:pk>', views.excluirCliente, name='excluiCliente'),
    path('editarcliente/<int:pk>', views.editarCliente, name='editarCliente'),
    path('excluidiarista/<int:pk>', views.excluirDiarista, name='excluiDiarista'),
    path('editardiarista/<int:pk>', views.editarDiarista, name='editarDiarista'),
    path('excluifuncionario/<int:pk>', views.excluirFuncionario, name='excluiFuncionario'),
    path('editarfuncionario/<int:pk>', views.editarFuncionario, name='editarFuncionario'),

    path('cadastroServico/',views.cadastroServico,name = 'cadastroServico'),
    path('cadastroCombo/', views.cadastroComboServico, name='cadastroCombo'),
    path('cadastroCategoria/', views.cadastroCategoriaCliente, name='cadastroCategoriaCliente'),
    path('listarCategoria/', views.listCategoriaCliente, name='listaCategoriaCliente'),
    path('cadastroCliente/', views.cadastroCliente, name='cadastroCliente'),
    path('listaCliente/', views.listClientes, name='listaClientes'),
    path('cadastroFuncionario/', views.cadastroFuncionario, name='cadastroFuncionario'),
    path('listarFuncionario/', views.listFuncionario, name='listaFuncionario'),
    path('cadastroDiarista/', views.cadastroDiarista, name='cadastroDiarista'),
    path('listaDiarista/', views.listDiarista, name='listaDiarista'),
    path('criarContrato/', views.criarContrato, name='criarContrato'),
    path('listaContrato/', views.listContrato, name='listaContrato'),
    path('lista-filtro/<filtro>/', views.resultadoPesquisa, name='listaFiltro'),


]
