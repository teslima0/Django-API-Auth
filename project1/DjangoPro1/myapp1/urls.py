
from django.urls import path
from .views import index, ApiOverView,Tasklist, TaskeDetails, CreateTask, UpdateTask, DeleteTask,GetAllProject,CreateProject
urlpatterns = [
    path('', index, name='homepage' ),
    path('list-task/', Tasklist, name='list-task' ),
    path('overview', ApiOverView, name='Api-view' ),
    path('task-details/<str:pk>', TaskeDetails, name='task-details' ),
    path('create-task', CreateTask, name='create-task'),
    path('task-update/<str:pk>', UpdateTask, name='task-update'),
    path('task-delete/<str:pk>', DeleteTask, name='task-delete'),
    #===========================project=====================================
    path('All-project/', GetAllProject, name='all-project'),
    path('CreateProject/', CreateProject, name='create-project'),
]
