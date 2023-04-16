from rest_framework import permissions


class IsTeacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role.pk == 2 or request.user.is_superuser
        

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True
            
            return request.user.is_superuser
        
        return False
    

class IsTeacherOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True

            return request.user.role.pk == 2 or request.user.is_superuser
        
        return False


class IsStudent(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.role.pk == 1
        
        return False
    


# class IsTeacherOrAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         try:
#             return request.user.role.pk == 2 or request.user.is_superuser

#         except:
#             return request.user.is_superuser