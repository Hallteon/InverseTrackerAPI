from django.contrib import admin
from news.models import New


class NewAdmin(admin.ModelAdmin):
    list_display = ('title', 'text')
    list_filter = ('title',)
    search_fields = ('title',)


admin.site.register(New, NewAdmin)