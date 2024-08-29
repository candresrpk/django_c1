from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
# Create your views here.


@login_required
def TasksView(request):
    tasks = Task.objects.filter(owner=request.user)
    # tasks = Task.objects.filter(owner=request.user, completed=True)
    
    context =  {
        'tasks': tasks
    }
    return render(request, 'tasks/tasks.html', context)


@login_required
def createTasksView(request):
    form = TaskForm
    
    context = {
        'form':  form
    } 
    
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', context)
        
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            
            return redirect('tasks:all_tasks')

        except Exception as e:
            context['error'] = str(e)
            return render(request, 'tasks/create_task.html', context)


@login_required
def editTasksView(request, id):
    task = get_object_or_404(Task, id=id)
    form = TaskForm( instance=task)
    
    context = {
        'task': task,
        'form': form
    }
    
    if request.method == 'GET':
        return render(request, 'tasks/edit_task.html', context)
    
    else:
        try:
            form = TaskForm(request.POST, instance=task)
            form.save()
            
            return redirect('tasks:all_tasks')
        except Exception as e:
            context['error'] = str(e)
            return render(request, 'tasks/edit_task.html', context)
    
    
@login_required
def completeTasksView(request, id):
    task = get_object_or_404(Task, id=id)
    task.completed = True    
    task.save()
    
    return redirect('tasks:all_tasks')


@login_required
def deleteTasksView(request, id):
    task = get_object_or_404(Task, id=id)
    task.delete()
    
    return redirect('tasks:all_tasks')
    