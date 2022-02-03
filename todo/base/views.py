"""Base app class based views"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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


class TaskCreate(CreateView):
    """Task creating view"""

    model = Task
    template_name = 'base/task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(UpdateView):
    """Task updating view"""

    model = Task
    template_name = 'base/task_update.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(DeleteView):
    """Task deleting view"""

    model = Task
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')
