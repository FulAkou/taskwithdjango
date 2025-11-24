from django.shortcuts import render
from .models import Category

# Create your views here.
def detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category/detail.html', {'category': category})
