from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import Class


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = get_user_model()
        fields = ('email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role', 'password')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role')


class ClassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Class
        fields = ('number', 'litera')