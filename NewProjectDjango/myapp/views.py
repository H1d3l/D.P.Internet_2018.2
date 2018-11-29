from django.shortcuts import render,redirect
from django.utils import timezone
from myapp.models import *
from myapp.forms import *
# Create your views here.

def list_post(request):
    posts = Post.objects.all().order_by('-data_published')
    return render(request,'list_post.html',{'posts':posts})

def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.data_published = timezone.now()
            model_instance.save()
            return redirect('list_post')
    else:
        form = PostForm()
        return render(request,'add_post.html',{'form':form})

