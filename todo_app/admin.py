from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'deadline', 'slug')
    list_filter = ('title', 'created', 'deadline')
    ordering = ('created',)
    date_hierarchy = 'created'
    prepopulated_fields = {"slug": ("title",), }
    search_fields = ('title', 'created')
