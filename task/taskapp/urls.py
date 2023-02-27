from django.urls import path
from .views import add_task, mark_task_complete, view_todo_list, delete_task

urlpatterns = [
    path('add_task/', add_task, name='add_task'),
    path('mark_task_complete/<int:task_id>/', mark_task_complete, name='mark_task_complete'),
    path('', view_todo_list, name='view_todo_list'),
    path('delete_task/<int:task_id>/', delete_task, name='delete_task'),
]
