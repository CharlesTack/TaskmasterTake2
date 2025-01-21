from django.shortcuts import render
from .models import Task

def home(request):
    """
    A view to display tasks to do and completed tasks
    with the tasks due soonest at the top
    """

    tasks_todo = Task.objects.filter(completed=False).order_by('due_date')
    tasks_done = Task.objects.filter(completed=True).order_by('due_date')
    return render(request, 'tasks/index.html', {'tasks_todo': tasks_todo, 'tasks_done': tasks_done})