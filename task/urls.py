from django.urls import path
from . import views


urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('edit_task/<int:pk>/', views.edit_task, name='edit_task'),
]
