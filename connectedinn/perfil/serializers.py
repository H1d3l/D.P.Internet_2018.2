from rest_framework import serializers
from perfil.models import Perfil

class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Perfil
        fields = ('nome','telefone','nome_empresa')



