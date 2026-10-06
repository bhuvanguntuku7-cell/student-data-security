from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    # Built-in Django Admin Interface
    path('admin/', admin.site.urls),

    # Core Application Views
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),

    # Authentication Management
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
]