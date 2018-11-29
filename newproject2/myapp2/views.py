from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from myapp2.models import *
from myapp2.forms import *

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


def edit_post(request,pk):
    editpost = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=editpost)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.author = request.user
            model_instance.data_published = timezone.now()
            model_instance.save()
            return redirect('list_post')
    else:
        form = PostForm(instance=editpost)
        return render(request, 'add_post.html', {'form': form})


