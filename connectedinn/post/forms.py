from django.forms import ModelForm
from post.models import *



class PostForm(ModelForm):
    class Meta:
        model = Postagem
        fields = '__all__'
