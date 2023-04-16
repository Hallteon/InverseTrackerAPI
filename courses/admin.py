from django.contrib import admin
from courses.models import *
from courses.forms import ScheduleForm


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher', 'category', 'place')
    list_filter = ('name', 'teacher')
    search_fields = ('name', 'teacher')


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'student',)
    list_filter = ('student',)
    search_fields = ('student',)


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'date')
    list_filter = ('task', 'date')
    search_fields = ('task', 'date')


class ScheduleAdmin(admin.ModelAdmin):
    form = ScheduleForm
    list_display = ('id', 'day', 'time')
    list_filter = ('day', 'time')
    search_fields = ('day', 'time')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_filter = ('name',)
    search_fields = ('name',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'limit', 'open')
    list_filter = ('name', 'limit', 'open')
    search_fields = ('name', 'limit', 'open')


class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'homework', 'date')
    list_filter = ('name', 'homework', 'date')
    search_fields = ('name', 'date')


admin.site.register(Course, CourseAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Homework, HomeworkAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Lesson, LessonAdmin)