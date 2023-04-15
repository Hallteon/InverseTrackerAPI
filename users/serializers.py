from urllib import request
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

from users.models import Role


class UserRegistrationSerializer(BaseUserRegistrationSerializer):

    class Meta(BaseUserRegistrationSerializer.Meta):
        model = get_user_model()
        fields = ('id', 'email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role', 'password')


class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('id', 'name')


class CustomUserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(required=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role')
