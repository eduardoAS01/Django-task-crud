from django.urls import path
from .views import CreateTask,ListTask,UpdateTask,DeleteTask

urlpatterns = [
    path('create/',CreateTask.as_view(),name='create_task'),
    path('list/',ListTask.as_view(),name='list_task'),
    path('update/<int:pk>',UpdateTask.as_view(),name='update_task'),
    path('delete/<int:pk>',DeleteTask.as_view(),name='delete_task')
]
