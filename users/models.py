from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class Class(models.Model):
    number = models.IntegerField(verbose_name='Цифра')
    litera = models.CharField(max_length=1, verbose_name='Литера')

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Role(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True)
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('firstname', 'Admin')
        extra_fields.setdefault('lastname', 'Admin')
        extra_fields.setdefault('patronymic', 'Admin')
        extra_fields.setdefault('age', 255)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    firstname = models.CharField(max_length=255, verbose_name='Имя')
    lastname = models.CharField(max_length=255, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=255, verbose_name='Отчество')
    age = models.IntegerField(verbose_name='Возраст')
    school_class = models.ForeignKey('Class', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Класс')
    role = models.ForeignKey('Role', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Роль')
    password = models.TextField(verbose_name='Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'