from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Task
from .form import TaskForm

class CreateTask(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/create.html'
    success_url = reverse_lazy('landing')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ListTask(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list.html'

    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)
    
class UpdateTask(UpdateView):
    model = Task
    fields = ['title','text','end_at','completed']
    template_name = 'task/update.html'
    success_url = reverse_lazy('landing')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'task/delete.html' 
    success_url = reverse_lazy('landing')   


class ListTaskComplete(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list_task_complete.html'
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user,completed = True)


class ListTaskNotComplete(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task/list_task_no_complete.html'
    
    def get_queryset(self):
        return Task.objects.filter(user = self.request.user,completed = False)

def complete_task(request,pk):
     task = get_object_or_404(Task,id=pk)
     task.completed = not task.completed
     task.save()
     return redirect('list_task')




