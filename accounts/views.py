from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserEditForm
from .models import CustomUser


# Create your views here.
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    model = CustomUser
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UserEditView(UpdateView):
    model = CustomUser
    form_class = UserEditForm
    template_name = "registration/user_edit.html"
    success_url = reverse_lazy("home")

    def get_object(self, queryset=None):
        pk = self.request.user.pk
        return self.model.objects.get(pk=pk)
