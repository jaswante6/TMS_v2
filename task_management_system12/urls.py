"""
URL configuration for task_management_system12 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from tasks.urls import urlpatterns as task_url
from tasks.views import complete_task,overdue_tasks,get_project_progress


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(task_url)),
    path('api/tasks/<int:id>/complete/', complete_task, name='complete_task'),
    path('tasks/overdue/', overdue_tasks, name='overdue_tasks'),
    path('projects/<int:pk>/progress/', get_project_progress, name='get_project_progress'),
]


    
    


    



