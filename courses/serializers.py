from rest_framework import serializers
from courses.models import Course, Application


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('name', 'description', 'mentor', 'members', 'time', 'category')


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = ('sender', 'course')
