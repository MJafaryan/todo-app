from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from tasks.models import TaskModel
from .filters import TaskModelFilters
from .serializers import TaskSerializer

class TasksListView(ListCreateAPIView):
    """The view for list and create TaskModel objects."""

    permission_classes = [IsAuthenticated,]
    serializer_class = TaskSerializer

    filter_backends = [DjangoFilterBackend,]
    filterset_class = TaskModelFilters

    def get_queryset(self):
        return TaskModel.objects.filter(user=self.request.user).order_by("-created_at")


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class TaskView(RetrieveUpdateDestroyAPIView):
    """The view for check, delete or, update TaskModel objects."""

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return TaskModel.objects.filter(user=self.request.user)

    def get_object(self):
        task_id = self.kwargs.get("pk")
        print("id:", task_id)
        task = get_object_or_404(TaskModel, id=task_id, user=self.request.user)
        return task
