from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("none", "None"),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="none")
    date_of_birth = models.DateField(_("birthday"), null=True)
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "email",
        "date_of_birth",
    ]

    def __str__(self):
        return self.username
