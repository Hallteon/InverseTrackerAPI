from django.db import models


class New(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Содержание')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'