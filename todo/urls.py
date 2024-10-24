from django.urls import path
from .views import HomePageView, TaskListView, TaskDetailView

urlpatterns = [
    path("tasks/<int:pk>/", TaskDetailView.as_view(), name="task_detail"),
    path("tasks/", TaskListView.as_view(), name="task_list"),
    path("", HomePageView.as_view(), name="home"),
]
