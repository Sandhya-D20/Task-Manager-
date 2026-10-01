from django.urls import path
from .views import home, update_task, toggle_todo, delete_task
urlpatterns=[
    path("", home, name="home"),
    path("task/<int:task_id>/update/", update_task, name="update_task"),
    path("todo/<int:todo_id>/toggle/", toggle_todo, name="toggle_todo"),
    path("task/<int:task_id>/delete/", delete_task, name="delete_task"),
]   