"""
URL configuration for task_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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

from task_app.views import get_tasks
from task_app.views import create_user
from task_app.views import add_user
from task_app.views import add_task
from task_app.views import get_users
from task_app.views import get_user_by_id
from task_app.views import get_task_by_id
from task_app.views import index
from django.urls import include
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", index),
    path("admin/", admin.site.urls),
    path("api/", include("task_app.calculator.urls")),
    path("jobs/", include("task_app.job_app.urls")),
    path("application/", include("task_app.application_app.urls")),
    path("task/add/", add_task),
    path("user/add/", add_user),
    path("user/create/", create_user),
    path("user/get/", get_users),
    path("user/get/<int:user_id>/", get_user_by_id),
    path("task/get/", get_tasks),
    path("task/get/<int:task_id>/", get_task_by_id),
]
