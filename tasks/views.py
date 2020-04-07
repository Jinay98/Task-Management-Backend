from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from tasks.models import Task
from tasks.serializers import TaskSerializer


@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(tasks_serializer.data, safe=False)

    elif request.method == 'POST':
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Task.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        task_serializer = TaskSerializer(task)
        return JsonResponse(task_serializer.data)

    elif request.method == 'PUT':
        project_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(task, data=project_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse(task_serializer.data)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

