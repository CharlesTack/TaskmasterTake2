from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task, Category
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

def index(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    
    tasks_todo = Task.objects.filter(completed=False).order_by('due_date')
    tasks_done = Task.objects.filter(completed=True).order_by('due_date')
    return render(request, 'tasks/index.html', {'form': form, 'tasks_todo': tasks_todo, 'tasks_done': tasks_done})

def home(request):
    tasks_todo = Task.objects.filter(completed=False).order_by('due_date')
    tasks_done = Task.objects.filter(completed=True).order_by('due_date')
    return render(request, 'tasks/index.html', {'tasks_todo': tasks_todo, 'tasks_done': tasks_done})

class TaskCreateView(CreateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completed', 'category']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('index')

class TaskUpdateView(UpdateView):
    model = Task
    fields = ['title', 'description', 'due_date', 'completed', 'category']
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('index')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('index')