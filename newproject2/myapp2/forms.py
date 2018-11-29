from myapp2.models import *
from django.forms import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        '''
        uma idiotice pois so usar o textfield no model ja basta
        '''
        widgets = {
            'text': Textarea(),
        }
        fields = ['title','text']
