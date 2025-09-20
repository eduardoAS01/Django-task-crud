from django.urls import path
from .views import CreateTask,ListTask,UpdateTask,DeleteTask,complete_task

urlpatterns = [
    path('create/',CreateTask.as_view(),name='create_task'),
    path('list/',ListTask.as_view(),name='list_task'),
    path('update/<int:pk>',UpdateTask.as_view(),name='update_task'),
    path('delete/<int:pk>',DeleteTask.as_view(),name='delete_task'),
    #path('list/completed/',ListTaskComplete.as_view(),name='list_task_completed'),
    path('complete/<int:pk>',complete_task,name='complete_task'),
    #path('list/notcompleted/',ListTaskNotComplete.as_view(),name='list_task_not_completed'),
    #path('list/bydate/',ListTaskByDate.as_view(),name='list_task_by_date')
]
