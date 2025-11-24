

from django.contrib import admin
from django.urls import path
from task.views import frontpage
from category.views import detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('<int:pk>/', detail, name='category_detail'),
]
