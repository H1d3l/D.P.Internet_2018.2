from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Game
from rest_framework.validators import UniqueTogetherValidator,UniqueValidator

class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')



    def validate(self,data):
        name_game = data['name']
        game = Game.objects.filter(name=name_game)
        if game.exists():
            raise serializers.ValidationError("Nome do jogo já existe")
        return data



