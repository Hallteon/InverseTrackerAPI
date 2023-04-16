from django.shortcuts import render
from news.serializers import NewSerializer
from rest_framework import generics
from news.models import New
from users.permissions import *


class NewAPIListCreateView(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permissions_classes = [IsTeacherOrAdminOrReadOnly]
    

class NewAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]