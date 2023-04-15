from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from users.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser, Role


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('id', 'email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role', 'is_superuser')
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role', 'password')}),
        ('Permissions', {'fields': ('is_superuser',)}),)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstname', 'lastname', 'patronymic', 'age', 'school_class', 'role', 'password1', 'password2'),
        }),)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Role, RoleAdmin)
admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)