from django.shortcuts import render

from .models import Task


# Create your views here.
def frontpage(request):

    title= "This is a Front Page"

    tasks = Task.objects.filter(is_done=True)

    return render(request, 'task/frontpage.html', {'title': title, 'tasks': tasks})
