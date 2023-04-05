from rest_framework import generics, status
from rest_framework.response import Response
from courses.models import Course, Application
from courses.permissions import IsTeacherOrAdminOrReadOnly, IsStudent
from courses.serializers import CourseSerializer, ApplicationSerializer
from users.permissions import IsTeacherOrAdmin


class CourseListCreateAPIView(generics.ListCreateAPIView):
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
    permission_classes = [IsStudent]


class ApplicationAPIList(generics.ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self):
        return Application.objects.filter(course=self.kwargs['pk'])


class ApplicationAPIConfirmView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsTeacherOrAdmin]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.course.members.add(instance.sender)
        instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ApplicationAPIRejectView(generics.DestroyAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsTeacherOrAdmin]



