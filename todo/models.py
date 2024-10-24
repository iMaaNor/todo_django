from django.db import models
from django.conf import settings
from django.urls import reverse_lazy


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    STATUS_CHOICES = (
        ("todo", "Todo"),
        ("doing", "Doing"),
        ("done", "Done"),
    )
    status = models.CharField(max_length=5, choices=STATUS_CHOICES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("task_detail", kwargs={"pk": self.pk})
