from django.db import models
from django_currentuser.db.models import CurrentUserField
from users.models import CustomUser


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    members = models.ManyToManyField(CustomUser, blank=True, related_name='courses', verbose_name='Участники')
    mentor = CurrentUserField(on_delete=models.CASCADE, verbose_name='Автор проекта')
    time = models.TextField(verbose_name='График')
    category = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Application(models.Model):
    sender = CurrentUserField(on_delete=models.CASCADE, verbose_name='Отправитель заявки')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, verbose_name='Курс')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'