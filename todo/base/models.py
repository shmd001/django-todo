"""Base app models"""

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    """Task Model"""

    user = models.ForeignKey(
        User, blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for ordering tasks"""

        ordering = ['-created']
