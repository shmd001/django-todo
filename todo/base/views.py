"""Base app class based views"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task


class TaskList(ListView):
    """Task list view"""

    model = Task
    context_object_name = 'tasks'


class TaskDetail(DetailView):
    """Task detail view"""

    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'
