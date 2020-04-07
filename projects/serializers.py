from rest_framework import serializers
from projects.models import Project


class ProjectSerializer(serializers.ModelSerializer):
    task_id = serializers.CharField(source='task.id')
    task_name = serializers.CharField(source='task.name')
    task_description = serializers.CharField(source='task.description')
    task_start_date = serializers.CharField(source='task.start_date')
    task_end_date = serializers.CharField(source='task.end_date')

    class Meta:
        model = Project
        fields = ('id', 'name',
                  'description',
                  'duration', 'task_id', 'task_name', 'task_description', 'task_start_date', 'task_end_date')
