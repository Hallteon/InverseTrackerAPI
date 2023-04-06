from rest_framework import serializers
from courses.models import Course, Application, Homework


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('name', 'description', 'teacher', 'members', 'time', 'category')


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('sender', 'course')


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('course', 'teacher', 'text', 'time')
