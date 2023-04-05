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
from courses.views import CourseListCreateAPIView, CourseAPIDetailView, ApplicationAPIConfirmView, ApplicationAPICreate, \
    ApplicationAPIList, ApplicationAPIRejectView
from users.views import ClassAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/courses/', CourseListCreateAPIView.as_view()),
    path('api/courses/<int:pk>/', CourseAPIDetailView.as_view()),
    path('api/courses/applications/', ApplicationAPICreate.as_view()),
    path('api/courses/applications/<int:pk>/', ApplicationAPIList.as_view()),
    path('api/courses/applications/confirm/<int:pk>/', ApplicationAPIConfirmView.as_view()),
    path('api/courses/applications/reject/<int:pk>/', ApplicationAPIRejectView.as_view()),
    path('api/classes/', ClassAPIView.as_view()),
    path('api/users/auth/', include('djoser.urls')),
    re_path(r'^api/users/auth/', include('djoser.urls.authtoken')),
]
