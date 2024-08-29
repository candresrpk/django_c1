from django.urls import path
from .views import TasksView, createTasksView, editTasksView, completeTasksView,deleteTasksView

app_name = 'tasks'


urlpatterns = [
    path('all/', TasksView, name='all_tasks'),
    path('create/', createTasksView, name='create_task'),
    path('edit/<int:id>/', editTasksView, name='edit_task'),
    path('complete/<int:id>/', completeTasksView, name='complete_task'),
    path('delete/<int:id>/', deleteTasksView, name='delete_task'),
    
    
]
