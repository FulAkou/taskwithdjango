from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "is_done")
    list_filter = ("is_done",)
    search_fields = ("title","description")

admin.site.register(Task, TaskAdmin)
