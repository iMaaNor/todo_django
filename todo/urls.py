from django.urls import path
from .views import (
    HomePageView,
    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskDeleteView,
    TaskUpdateView,
    NoteEditView,
    NoteDeleteView,
)

urlpatterns = [
    path("notes/<int:pk>/edit/", NoteEditView.as_view(), name="note_edit"),
    path("notes/<int:pk>/delete/", NoteDeleteView.as_view(), name="note_delete"),
    path("tasks/add/", TaskCreateView.as_view(), name="task_add"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_edit"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("", HomePageView.as_view(), name="home"),
]
