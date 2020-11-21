from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_app:task_list')
    else:
        form = TaskForm()

    context = {'tasks': tasks,
               'form': form}

    return render(request,
                  'todo_app/task_list.html',
                  context)


def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()

    return redirect('todo_app:task_list')
