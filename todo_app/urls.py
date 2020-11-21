from django.urls import path
from . import views

app_name = 'todo_app'

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/', views.delete_task, name='delete_task')
]
