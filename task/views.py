from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from category.models import Category
from .forms import TaskForm

# Create your views here.
@login_required
def frontpage(request):
    title= "This is a Front Page"
    tasks = Task.objects.filter(user=request.user).filter(is_done=False)
    categories = Category.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('frontpage')
    else:
        form = TaskForm()

    return render(request, 'task/frontpage.html', {'title': title, 'tasks': tasks, 'categories': categories, 'form': form})

@login_required
def search(request):
    query = request.GET.get('query','')

    if query:
        tasks =Task.objects.filter(user=request.user).filter(Q(title__icontains=query) | Q(description__icontains=query))
    else:
        tasks = []

    return render(request, 'task/search.html', {'query': query, 'tasks': tasks})


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('frontpage')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task/edit.html', {'form': form})

@login_required
def mark_completed(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_done = True
    task.save()
    return redirect('frontpage')

@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('frontpage')
