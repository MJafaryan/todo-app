from django.urls import path
from .views import TasksListView, TaskView


urlpatterns = [
    path("", TasksListView.as_view(), name="tasks-list"),
    path("<int:pk>/", TaskView.as_view(), name="task"),
]
