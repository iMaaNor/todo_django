from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "gender",
            "email",
            "date_of_birth",
        )
        widgets = {"date_of_birth": forms.widgets.DateInput(attrs={"type": "date"})}


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "first_name",
            "last_name",
            "gender",
            "email",
            "date_of_birth",
        )
        widgets = {"date_of_birth": forms.widgets.DateInput(attrs={"type": "date"})}
