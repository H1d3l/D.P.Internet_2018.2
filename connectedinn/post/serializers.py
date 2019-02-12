from rest_framework import serializers
from post.models import *

class PostSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Postagem
        fields = ('text',)
