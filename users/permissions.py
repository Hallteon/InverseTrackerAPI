from rest_framework import permissions


class IsTeacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return request.user.role.pk == 2 or request.user.is_superuser

        except:
            return request.user.is_superuser