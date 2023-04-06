from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from courses.models import Course, Application, Homework
from courses.permissions import IsTeacherOrAdminOrReadOnly, IsStudent
from courses.serializers import CourseSerializer, ApplicationSerializer, HomeworkSerializer
from users.permissions import IsTeacherOrAdmin


class CourseAPIListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class CourseAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class ApplicationAPICreate(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsStudent]


class ApplicationAPIList(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdminOrReadOnly]

    def get_queryset(self):
        return Application.objects.filter(course=self.kwargs['pk'])


class ApplicationAPIConfirmView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.course.members.add(instance.sender)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationAPIRejectView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]


class HomeworkAPICreateView(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdmin]


class HomeworkAPIListView(generics.ListAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Homework.objects.filter(course=self.kwargs['pk'])


class HomeworkAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsAuthenticated, IsTeacherOrAdminOrReadOnly]