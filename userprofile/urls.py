from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='userprofile/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(), name='signout'),
]
