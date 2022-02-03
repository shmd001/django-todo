"""Base app class based views"""

from .models import Task
from django.views.generic.list import ListView


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
