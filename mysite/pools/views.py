from django.shortcuts import render
from django.http import HttpResponse
from pools.models import *
# Create your views here.
def index(request):
    return render(request,'index.html',{'questions':Question.objects.all()})


def exibir_question(request,id_question):
    return render(request,'question.html',{'question':Question.objects.get(id=id_question)})
