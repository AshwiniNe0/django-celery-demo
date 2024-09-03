from django.urls import path
from .views import start_task, task_status, index

urlpatterns = [
    path('', index, name='index'),
    path('start-task/', start_task, name='start_task'),
    path('task-status/<str:task_id>/', task_status, name='task_status'),
]