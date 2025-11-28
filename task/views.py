from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from category.models import Category
from .forms import TaskForm

# Create your views here.
def frontpage(request):
    title= "This is a Front Page"
    tasks = Task.objects.filter(is_done=False)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = TaskForm()

    return render(request, 'task/frontpage.html', {'title': title, 'tasks': tasks, 'categories': categories, 'form': form})


def search(request):
    query = request.GET.get('query','')

    if query:
        tasks =Task.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        tasks = []

    return render(request, 'task/search.html', {'query': query, 'tasks': tasks})



def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task/edit.html', {'form': form})


def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect('frontpage')


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('frontpage')
