from django.db import models

from category.models import Category

# Create your models here.
class Task(models.Model):
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    is_done = models.BooleanField(default=False)
