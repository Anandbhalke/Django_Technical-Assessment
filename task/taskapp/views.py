from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Task

def add_task(request):
    if request.method == 'POST':
        description = request.POST['description']
        task = Task(description=description)
        task.save()
        return redirect('view_todo_list')
    return render(request, 'add_task.html')

def mark_task_complete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    return redirect('view_todo_list')


def view_todo_list(request):
    tasks = Task.objects.filter(completed=False)
    return render(request, 'view_todo_list.html', {'tasks': tasks})



def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('view_todo_list')

