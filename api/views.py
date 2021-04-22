from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from api.models import TaskList, TaskItem
from api.serializers import TaskListSerializer, TaskItemSerializer


class TaskListView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = TaskListSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class TaskListDetail(generics.DestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = TaskListSerializer

    def destroy(self, request, *args, **kwargs):
        pk = kwargs['pk']
        queryset = TaskList.objects.get(id=pk)
        self.perform_destroy(queryset)
        return Response({"message:": "deleted list"})


class TaskItemView(generics.ListCreateAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = TaskItem.objects.all()
    serializer_class = TaskItemSerializer

    def list(self, request, *args, **kwargs):
        tasks_pk = kwargs['pk']
        queryset = TaskItem.objects.filter(tasklist=tasks_pk)
        serializer = TaskItemSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save()


class TaskItemDetailed(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    queryset = []
    serializer_class = TaskItemSerializer

    def destroy(self, request, *args, **kwargs):
        taskid_pk = kwargs['pk']
        queryset = TaskItem.objects.get(task_id=taskid_pk)
        self.perform_destroy(queryset)
        return Response({"message:": "deleted task"})

    def update(self, request, *args, **kwargs):
        taskid_pk = kwargs['pk']
        partial = kwargs.pop('partial', False)
        instance = TaskItem.objects.get(task_id=taskid_pk)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
