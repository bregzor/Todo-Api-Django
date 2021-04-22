from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api.models import TaskList, TaskItem


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskList
        fields = '__all__'


class TaskItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskItem
        fields = ["task_id", 'title', "description", "tasklist", "isCompleted"]
