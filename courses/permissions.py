from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS


class IsTeacherOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request in SAFE_METHODS:
            return True

        try:
            return request.user.role.pk == 2 or request.user.is_superuser

        except:
            return request.user.is_superuser


class IsStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.role.pk == 1

