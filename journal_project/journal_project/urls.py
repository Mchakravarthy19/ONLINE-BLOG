"""
URL configuration for journal_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from journal_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('journals/', views.journal_list, name='journal_list'),
    path('journals/<int:pk>/', views.journal_detail, name='journal_detail'),
    path('journals/create/', views.journal_create, name='journal_create'),
    path('journals/<int:pk>/edit/', views.journal_update, name='journal_update'),
    path('journals/<int:pk>/delete/', views.journal_delete, name='journal_delete'),
    path('feedback/', views.feedback_view, name='feedback'),
]

