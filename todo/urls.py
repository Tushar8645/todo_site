from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.createTodo, name='create_todo'),
    path('current/', views.currentTodo, name='current_todo'),
    path('completed/', views.completedTodo, name='completed_todo'),
    path('todo/<int:todo_pk>/', views.viewTodo, name='view_todo'),
    path('completed/<int:todo_pk>/',
         views.taskAccomplished, name='task_accomplished'),
    path('delete/<int:todo_pk>/', views.deleteTodo, name='delete_todo'),
]
