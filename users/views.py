from rest_framework import generics
from users.models import Class
from users.permissions import IsTeacherOrAdmin
from users.serializers import ClassSerializer


class ClassAPIView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [IsTeacherOrAdmin]
