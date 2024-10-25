from django.contrib import admin
from .models import Task, Note


# Register your models here.
class NoteInline(admin.TabularInline):
    model = Note
    extra = 1


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
    inlines = [NoteInline]
