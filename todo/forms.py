from django import forms
from .models import Task, Note


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            "title",
            "description",
            "status",
            "due_date",
        ]
        widgets = {
            "due_date": forms.widgets.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            "note",
        ]
