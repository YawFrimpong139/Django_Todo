from django.shortcuts import redirect, render
from . models import Todolist

# Create your views here.
def home(request):
    tasks = Todolist.objects.all().order_by('-id')
    return render(request, 'index.html', {'tasks': tasks})


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        due_time = request.POST.get('due_time')
        completed = False
        
        if title != '' and due_date != '' and due_time != '':
            task = Todolist(
                title=title, 
                description=description,
                due_date=due_date, 
                due_time=due_time,
                completed=completed
            )
            task.save()
            return redirect('home')
    else:        
        return render(request, 'add_task.html')


def completed(request):
    completed_task = Todolist.objects.filter(completed=True)
    return render(request, 'completed.html', {'tasks': completed_task})

def delete(request, task_id):
    task = Todolist.objects.get(id=task_id)
    return render(request, 'delete.html', {"task": task})

def remaining(request):
    remaining_task = Todolist.objects.filter(completed=False)
    return render(request, 'remaining.html', {"tasks" : remaining_task})

def task_detail(request, task_id):
    task = Todolist.objects.get(id=task_id)
    return render(request, 'task_detail.html', {"task" : task})

def toggle_complete(request, task_id):
    task = Todolist.objects.get(id=task_id)
    if task:
        task.completed = not task.completed
        task.save()
        return redirect('home')

def remove_task(request, task_id):
    task = Todolist.objects.get(id=task_id)
    if task:
        task.delete()
        return redirect('home')

