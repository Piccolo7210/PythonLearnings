from django.urls import path
from .views import task_list, task_create, task_update, task_delete, task_toggle_complete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('update/<int:pk>/', task_update, name='task_update'),
    path('delete/<int:pk>/', task_delete, name='task_delete'),
    path('toggle/<int:pk>/', task_toggle_complete, name='task_toggle_complete'),
]