"""
URL configuration for inverse_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from courses.views import *
from users.views import *
from news.views import NewAPIListCreateView, NewAPIDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/courses/', CourseAPIListCreateView.as_view()),
    path('api/courses/category/<int:pk>/', CourseAPICategoryListView.as_view()),
    path('api/courses/<int:pk>/', CourseAPIDetailView.as_view()),
    path('api/courses/categories/', CategoryAPIListCreateView.as_view()),
    path('api/courses/categories/<int:pk>/', CategoryAPIDetailView.as_view()),
    path('api/courses/groups/<int:pk>/applications/send/', ApplicationAPICreateView.as_view()),
    path('api/courses/groups/<int:pk>/applications/', ApplicationAPIListView.as_view()),
    path('api/courses/groups/<int:group_pk>/applications/confirm/<int:pk>/', ApplicationAPIConfirmView.as_view()),
    path('api/courses/groups/<int:group_pk>/applications/reject/<int:pk>/', ApplicationAPIRejectView.as_view()),
    path('api/courses/<int:pk>/groups/create/', GroupAPICreateView.as_view()),
    path('api/courses/groups/<int:pk>/', GroupAPIDetailView.as_view()),
    path('api/courses/groups/<int:pk>/schedules/create/', ScheduleAPICreateView.as_view()),
    path('api/courses/groups/schedules/<int:pk/', ScheduleAPIDetailView.as_view()),
    path('api/courses/groups/<int:pk>/lessons/create/', LessonAPICreateView.as_view()),
    path('api/courses/groups/lessons/<int:pk>/attendings/', LessonAPIAddAttending.as_view()),
    path('api/courses/groups/lessons/<int:pk>/', LessonAPIDetailView.as_view()),
    path('api/courses/groups/lessons/<int:pk>/homeworks/create/', HomeworkAPICreateView.as_view()),
    path('api/courses/groups/lessons/homeworks/<int:pk>/passed/', HomeworkAPIAddPassed.as_view()),
    path('api/courses/groups/lessons/homeworks/<int:pk>/', HomeworkAPIDetailView.as_view()),
    path('api/news/', NewAPIListCreateView.as_view()),
    path('api/news/<int:pk>/', NewAPIDetailView.as_view()),
    path('api/users/auth/', include('djoser.urls')),
    path('api/users/me/groups/', GroupAPIMeListView.as_view()),
    path('api/users/me/skips/', LessonAPISkipsListView.as_view()),
    path('api/users/me/doubts/', HomeworkAPIDoubtsListView.as_view()),
    path('api/users/me/teacher/courses/', CourseAPIMeTeacherListView.as_view()),
    path('api/users/me/student/courses/', CourseAPIMeStudentListView.as_view()),
    re_path(r'^api/users/auth/', include('djoser.urls.authtoken')),
]
