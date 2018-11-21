from django.shortcuts import render
from django.http import HttpResponse
from pools.models import *
# Create your views here.
def index(request):
    questions = Question.objects.all()
    print(questions)
    return render(request,'index.html',{'questions':Question.objects.all()})


def exibir_question(request,question_id):
    return render(request, 'question.html', {'questions': Question.objects.get(id=question_id)})

