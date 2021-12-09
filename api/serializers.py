from rest_framework import serializers
from .models import Specialite, Resto
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user


class RestoSerializer(serializers.ModelSerializer):

    class Meta:
        ordering = ['-id']
        model = Resto
        fields = ('id', 'nom', 'adresse', 'code_postal', 'ville', 'pays', 'halal', 'instagram', 'tripadvisor', 'user', 'specialites')
        extra_kwargs = {'specialites': {'required': False}}


class SpecialiteSerializer(serializers.ModelSerializer):
    restos = RestoSerializer(many=True, read_only=True)

    class Meta:
        ordering = ['-id']
        model = Specialite
        fields = ("id", "nom", "restos")
        extra_kwargs = {'restos': {'required': False}}