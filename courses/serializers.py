from rest_framework import serializers
from courses.models import Course, Application, Homework, Lesson, Group, Schedule, Category
from users.serializers import CustomUserSerializer
from drf_extra_fields.fields import Base64ImageField, Base64FileField
import logging
import io
import PyPDF2


class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf']

    def get_file_extension(self, filename, decoded_file):
        try:
            PyPDF2.PdfReader(io.BytesIO(decoded_file))

        except PyPDF2.errors.PdfReadError as e:
            logging.warning(e)

        else:
            return 'pdf'


class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Schedule
        fields = ('id', 'day', 'time')


class ApplicationGetSerializer(serializers.ModelSerializer):
    student = CustomUserSerializer(required=False)

    class Meta:
        model = Application
        fields = ('id', 'student', 'status')


class ApplicationPostSerializer(serializers.ModelSerializer):
    student = CustomUserSerializer(required=False)
    document = PDFBase64File(represent_in_base64=True)

    class Meta:
        model = Application
        fields = ('id', 'student', 'document', 'status')


class ApplicationDocumentSerializer(serializers.ModelSerializer):
    document = PDFBase64File(represent_in_base64=True)

    class Meta:
        model = Course
        fields = ('id', 'document')


class HomeworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homework
        fields = ('id', 'task', 'date', 'passed')


class LessonSerializer(serializers.ModelSerializer):
    homework = HomeworkSerializer()
    attendings = CustomUserSerializer(many=True)

    class Meta:
        model = Lesson
        fields = ('id', 'name', 'homework', 'attendings', 'date')


class GroupSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True, required=False)
    members = CustomUserSerializer(many=True, required=False)
    lessons = LessonSerializer(many=True, required=False)
    applications = ApplicationGetSerializer(many=True, required=False)

    class Meta:
        model = Group
        fields = ('id', 'name', 'schedule', 'members', 'lessons', 'applications', 'limit', 'open')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name')


class CourseGetSerializer(serializers.ModelSerializer):
    teacher = CustomUserSerializer()
    groups = GroupSerializer(many=True, required=False)
    category = CategorySerializer()
    image = Base64ImageField(represent_in_base64=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'teacher', 'groups', 'category', 'place', 'image',)


class CoursePostSerializer(serializers.ModelSerializer):
    teacher = CustomUserSerializer()
    groups = GroupSerializer(many=True, required=False)
    category = CategorySerializer()
    image = Base64ImageField(represent_in_base64=True)
    document = PDFBase64File(represent_in_base64=True)

    def create(self, validated_data):
        image = validated_data.pop('image')
        data = validated_data.pop('data')

        return Course.objects.create(data=data, image=image)

    class Meta:
        model = Course
        fields = ('id', 'name', 'description', 'teacher', 'groups', 'category', 'place', 'image', 'document')


class CourseDocumentSerializer(serializers.ModelSerializer):
    document = PDFBase64File(represent_in_base64=True)

    class Meta:
        model = Course
        fields = ('id', 'document')