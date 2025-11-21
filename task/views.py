from django.shortcuts import render

from .models import Task
from category.models import Category

# Create your views here.
def frontpage(request):
    title= "This is a Front Page"
    tasks = Task.objects.filter(is_done=True)
    categories = Category.objects.all()

    return render(request, 'task/frontpage.html', {'title': title, 'tasks': tasks, 'categories': categories})
