from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Game
		fields = ('pk','name', 'release_date', 'game_category')