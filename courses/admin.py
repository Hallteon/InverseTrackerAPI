from django.contrib import admin
from courses.models import Course, Application, Homework


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'time', 'category')
    list_filter = ('name', 'teacher')
    search_fields = ('name',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'course')
    list_filter = ('sender', 'course')
    search_fields = ('sender', 'course')


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('course', 'teacher', 'text', 'time')
    list_filter = ('course', 'teacher')
    search_fields = ('course', 'teacher')


admin.site.register(Course, CourseAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Homework, HomeworkAdmin)