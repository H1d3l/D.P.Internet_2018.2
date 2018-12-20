from django.shortcuts import render,redirect
from book.models import *
from book.forms import *
# Create your views here.

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance = form.save()
            return redirect('list_author')
