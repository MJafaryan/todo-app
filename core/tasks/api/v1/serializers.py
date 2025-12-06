from rest_framework import serializers
from tasks.models import TaskModel

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = ("title", "description", "is_complete", "due_time",)
