from django.shortcuts import render,redirect
from core.models import *
from core.forms import *
# Create your views here.

def listaServico(request):
    return render(request, 'listaservico.html', {'servicos': Servico.objects.all()})


def cadastroServico(request):
    if request.method == 'POST':
        form = CadastroServicoForm(request.POST)
        if form.is_valid():
            model_instance = form.save()
            return redirect('listaServico')
    else:
        form = CadastroServicoForm()
        return render(request, 'add_servico.html', {'form':form})



