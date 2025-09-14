from django.shortcuts import render
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
    fields = ['title','text','end_at','done_it']
    template_name = 'task/update.html'
    success_url = reverse_lazy('landing')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'task/delete.html' 
    success_url = reverse_lazy('landing')   
