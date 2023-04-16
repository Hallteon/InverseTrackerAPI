from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import FileUploadParser
from courses.models import *
from courses.serializers import * 
from users.permissions import *
from inverse_tracker.settings import BASE_DIR


class CourseAPIListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseGetSerializer
    permission_classes = [IsAuthenticated]


class CourseAPICreateView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePostSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class CourseAPICategoryListView(generics.ListAPIView):
    serializer_class = CourseGetSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        return Course.objects.filter(category=self.kwargs['pk'])


class CourseAPIUpdateDestroyView(generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePostSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class CourseAPIRetrieveView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseGetSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class CourseAPIRetrieveDocumentView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDocumentSerializer
    permission_classes = [IsAuthenticated]


class ApplicationAPICreateView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationPostSerializer
    permission_classes = [IsStudent]

    def post(self, request, *args, **kwargs):
        serializer = ApplicationPostSerializer(data=request.data)

        if serializer.is_valid():
            group = Group.objects.get(pk=self.kwargs['pk'])

            if group.applications.filter(student=self.request.user.pk, status=2).exists() == False:
                serializer.save()
                group.applications.add(int(serializer.data['id']))
                group.save()

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            else:
                return Response({'error': 'Вы уже отправили заявку в эту группу!'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ApplicationAPIListView(generics.ListAPIView):
    serializer_class = ApplicationGetSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self):
        return Group.objects.get(pk=self.kwargs['pk']).applications


# class ApplicationAPIMeListView(generics.ListAPIView):
#     serializer_class = ApplicationGetSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         return Group.objects.get(pk=self.kwargs['pk']).applications


class ApplicationAPIConfirmView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationGetSerializer
    permission_classes = [IsTeacherOrAdmin]

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        group = Group.objects.get(pk=self.kwargs['group_pk'])

        if group.members.count() < int(group.limit):
            obj.status = 2
            group.members.add(obj.student.pk)
            group.save()
            obj.save()
            
        else:
            group.open = False
            group.save()

        serializer = ApplicationGetSerializer(obj)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    

class ApplicationAPIRejectView(generics.UpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationGetSerializer
    permission_classes = [IsTeacherOrAdmin]

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.status = 3

        obj.save()

        serializer = ApplicationGetSerializer(obj)

        return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)


class ApplicationAPIRetrieveDocumentView(generics.RetrieveAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationDocumentSerializer
    permission_classes = [IsAuthenticated]


class CategoryAPIListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class CategoryAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


class GroupAPICreateView(generics.CreateAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = GroupSerializer(many=True, data=request.data)

        if serializer.is_valid():
            serializer.save()
            
            course = Course.objects.get(pk=self.kwargs['pk'])
            course.groups.add(int(serializer.data['id']))
            course.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupAPIListView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        return Course.objects.get(pk=self.kwargs['pk']).groups


class GroupAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class ScheduleAPICreateView(generics.CreateAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = ScheduleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            group = Group.objects.get(pk=self.kwargs['pk'])
            group.schedule.add(serializer.data['id'])
            group.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleAPIListView(generics.ListAPIView):
    serializer_class = ScheduleSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        return Group.objects.get(pk=kwargs['pk']).schedule


class ScheduleAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class LessonAPICreateView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = LessonSerializer(data=request.data, required=False)

        if serializer.is_valid():
            serializer.save()

            group = Group.objects.get(pk=self.kwargs['pk'])

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LessonAPIAddAttending(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsTeacherOrAdmin]

    def update(self, request, *args, **kwargs):
        obj = Lesson.objects.get(pk=self.kwargs['pk'])
        attendings = request.GET.get('attendings', None)
        attendings_list = []

        if attendings is not None:
            for attend in attendings.split(','):
                attendings_list.append(int(attend))

        obj.attendings.add(*attendings_list)
        obj.save()

        serializer = LessonSerializer(obj, required=False)

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)


class LessonAPIListView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]

    def get_queryset(self):
        return Lesson.objects.filter(group=self.kwargs['pk'])


class LessonAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]


class HomeworkAPICreateView(generics.CreateAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsTeacherOrAdmin]

    def post(self, request, *args, **kwargs):
        serializer = HomeworkSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            lesson = Lesson.objects.get(pk=self.kwargs['pk'])
            lesson.homework = Homework.objects.get(pk=int(serializer.data['id']))
            lesson.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class HomeworkAPIAddPassed(generics.UpdateAPIView):
    serializer_class = HomeworkSerializer
    permission_classes = [IsTeacherOrAdmin]

    def update(self, request, *args, **kwargs):
        obj = Homework.objects.get(pk=self.kwargs['pk'])
        passeds = request.GET.get('passed', None)
        passed_list = []

        if passeds is not None:
            for passed in passeds.split(','):
                passed_list.append(int(passed))

        obj.passed.add(*passed_list)
        obj.save()

        serializer = HomeworkSerializer(obj, required=False)

        return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)


class HomeworkAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsTeacherOrAdminOrReadOnly]