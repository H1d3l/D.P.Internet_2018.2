from myapp.models import *
from django.forms import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']
