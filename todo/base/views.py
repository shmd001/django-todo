"""Base app class based views"""

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task


class UserSignin(LoginView):
    """User login view"""

    redirect_authenticated_user = True
    next_page = reverse_lazy('tasks')
    template_name = 'base/signin.html'


class UserSignout(LogoutView):
    """User logout view"""

    next_page = reverse_lazy('signin')


class TaskList(LoginRequiredMixin, ListView):
    """Task list view"""

    model = Task
    context_object_name = 'tasks'


class TaskDetail(LoginRequiredMixin, DetailView):
    """Task detail view"""

    model = Task
    template_name = 'base/task.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    """Task creating view"""

    model = Task
    template_name = 'base/task_create.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    """Task updating view"""

    model = Task
    template_name = 'base/task_update.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class TaskDelete(LoginRequiredMixin, DeleteView):
    """Task deleting view"""

    model = Task
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('tasks')
