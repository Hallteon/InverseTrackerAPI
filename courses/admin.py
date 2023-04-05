from django.contrib import admin
from courses.models import Course, Application


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'mentor', 'time', 'category')
    list_filter = ('name', 'mentor')
    search_fields = ('name',)


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'course')
    list_filter = ('sender', 'course')
    search_fields = ('sender', 'course')


admin.site.register(Course, CourseAdmin)
admin.site.register(Application, ApplicationAdmin)
