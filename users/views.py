from rest_framework import generics
from users.permissions import *
from courses.serializers import *
from courses.models import *
from rest_framework.permissions import IsAuthenticated


class CourseAPIMeStudentListView(generics.ListAPIView):
    serializer_class = CourseGetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user_groups = Group.objects.filter(members__in=[self.request.user.pk])
        groups = []

        for group in user_groups.all():
            groups.append(group.pk)

        user_courses = Course.objects.filter(groups__in=groups)

        return user_courses


class CourseAPIMeTeacherListView(generics.ListAPIView):
    serializer_class = CourseGetSerializer
    permission_classes = [IsTeacherOrAdmin]

    def get_queryset(self, *args, **kwargs):
        teacher_courses = Course.objects.filter(teacher=self.request.user.pk)

        return teacher_courses


class GroupAPIMeListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user_groups = Group.objects.filter(members__in=[self.request.user.pk])

        return user_groups


class LessonAPISkipsListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user_groups = Group.objects.filter(members__in=[self.request.user.pk])
        skip_lessons = []
        
        for group in user_groups.all():
            for lesson in group.lessons.all():
                if lesson.attendings.filter(pk=self.request.user.pk).exists() == False:
                    skip_lessons.append(lesson.pk)

        return Lesson.objects.filter(pk__in=skip_lessons)


class HomeworkAPIDoubtsListView(generics.ListAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user_groups = Group.objects.filter(members__in=[self.request.user.pk])
        doubts = []
        
        for group in user_groups.all():
            for lesson in group.lessons.all():
                if lesson.homework.passed.filter(pk=self.request.user.pk).exists() == False:
                    doubts.append(lesson.homework.pk)

        return Homework.objects.filter(pk__in=doubts)