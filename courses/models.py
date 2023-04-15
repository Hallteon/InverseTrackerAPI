import datetime
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.db import models
from django_currentuser.db.models import CurrentUserField
from users.models import CustomUser


class Schedule(models.Model):
    day = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)], verbose_name='День недели')
    time = models.TimeField(auto_now=False, auto_now_add=False, verbose_name='Время проведения')

    def __str__(self):
        return str(self.day) + ' день недели - ' + str(self.time)

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Group(models.Model):
    name = models.CharField(unique=True, max_length=255, verbose_name='Название')
    schedule = models.ManyToManyField('Schedule', blank=True, verbose_name='Расписание')
    members = models.ManyToManyField(CustomUser, blank=True, verbose_name='Участники группы')
    lessons = models.ManyToManyField('Lesson', blank=True, verbose_name='Уроки')
    applications = models.ManyToManyField('Application', blank=True, related_name='group', verbose_name='Заявки')
    limit = models.IntegerField(blank=True, verbose_name='Лимит')
    open = models.BooleanField(default=True, verbose_name='Открыт')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    teacher = CurrentUserField(on_delete=models.CASCADE, verbose_name='Автор курса')
    groups = models.ManyToManyField('Group', blank=True, related_name='course', verbose_name='Группы')
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, verbose_name='Категория')
    place = models.CharField(max_length=255, verbose_name='Место проведения')
    image = models.ImageField(blank=True, null=True, upload_to='courses/images/', verbose_name='Картинка')
    document = models.FileField(blank=True, null=True, upload_to='courses/documents/courses/', verbose_name='Документ')

    def __str__(self):
        return self.name
        
    def admin_image(self):
        return '<img src="%s"/>' % self.image

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Application(models.Model):
    student = CurrentUserField(on_delete=models.CASCADE, verbose_name='Отправитель заявки')
    document = models.FileField(blank=True, null=True, upload_to='courses/documents/applications/', verbose_name='Заполненный документ')
    status = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], default=1, verbose_name='Статус заявки')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Homework(models.Model):
    task = models.TextField(verbose_name='Задание')
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name='Время выполнения')
    passed = models.ManyToManyField(CustomUser, blank=True, verbose_name='Сдали')

    def __str__(self):
        return self.task[:20]

    class Meta:
        verbose_name = 'Домашняя работа'
        verbose_name_plural = 'Домашние работы'


class Lesson(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название урока')
    homework = models.ForeignKey('Homework', blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Домашка')
    attendings = models.ManyToManyField(CustomUser, blank=True, verbose_name='Присутствующие')
    date = models.DateField(auto_now=False, auto_now_add=False, blank=True, verbose_name='Дата урока')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
