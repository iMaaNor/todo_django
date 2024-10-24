from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "due_date",
        "status",
        "user",
    ]
    list_filter = [
        "status",
        "due_date",
    ]
    search_fields = [
        "title",
        "description",
    ]
