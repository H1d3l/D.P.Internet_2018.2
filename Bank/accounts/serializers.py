from rest_framework import serializers
from accounts.models import *




class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = '__all__'

    def validate(self,balance):
        balance_current = balance['balance']
        if balance_current < 0:
            raise serializers.ValidationError('Não pode valor negativo')
        return balance
