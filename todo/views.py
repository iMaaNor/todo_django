from django.http import HttpRequest, HttpResponse
from django.views import View
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
    FormView,
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .forms import TaskForm, NoteForm
from .models import Task, Note


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task_list.html"

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class NoteGet(UserPassesTestMixin, DetailView):
    model = Task
    template_name = "task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NoteForm
        return context

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user


class NotePost(SingleObjectMixin, FormView):
    model = Task
    form_class = NoteForm
    template_name = "task_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        note = form.save(commit=False)
        note.task = self.object
        note.save()
        return super().form_valid(form)

    def get_success_url(self):
        task = self.object
        return reverse("task_detail", kwargs={"pk": task.pk})


class TaskDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = NoteGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = NotePost.as_view()
        return view(request, *args, **kwargs)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_add.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = "task_delete.html"
    success_url = reverse_lazy("task_list")

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_edit.html"

    def test_func(self):
        object = self.get_object()
        return object.user == self.request.user


class NoteEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Note
    fields = ["note"]
    template_name = "note_edit.html"

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.object.task.pk})

    def test_func(self):
        object = self.get_object()
        return object.task.user == self.request.user


class NoteDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Note
    template_name = "note_delete.html"

    def get_success_url(self):
        return reverse("task_detail", kwargs={"pk": self.object.task.pk})

    def test_func(self):
        object = self.get_object()
        return object.task.user == self.request.user
