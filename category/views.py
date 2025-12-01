from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Category

# Create your views here.
@login_required
def detail(request, pk):
    category = Category.objects.get(pk=pk)
    return render(request, 'category/detail.html', {'category': category})
