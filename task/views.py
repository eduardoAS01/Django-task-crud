from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task
from .form import TaskForm

class CreateTask(LoginRequiredMixin,CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create.html'
    success_url = reverse_lazy('list_task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListTask(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list.html'

    def get_queryset(self):
        query_set = Task.objects.filter(user=self.request.user)

        status = self.request.GET.get("status")
        if status == "completed":
            query_set = query_set.filter(is_completed=True)
        elif status == "not-completed":
            query_set = query_set.filter(is_completed=False)

        order_by = self.request.GET.get("order_by")
        if order_by == "due_date":
            query_set = query_set.order_by("due_date")

        return query_set
    
class UpdateTask(LoginRequiredMixin,UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/update.html'
    success_url = reverse_lazy('list_task')

class DeleteTask(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'task/delete.html' 
    success_url = reverse_lazy('list_task')   

"""
class ListTaskComplete(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list_task_complete.html'
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user,is_completed = True)


class ListTaskNotComplete(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list_task_no_complete.html'
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user,is_completed = False)
    
class ListTaskByDate(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list_task_by_date.html'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('due_date')

"""

def complete_task(request,pk):
     task = get_object_or_404(Task,id=pk)
     task.is_completed = not task.is_completed
     task.save()
     return redirect('list_task')




