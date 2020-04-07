from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from projects.models import Project
from tasks.models import Task
from tasks.serializers import TaskSerializer
import datetime


@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)

        return JsonResponse(tasks_serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            task_data = JSONParser().parse(request)
            task_name = task_data.get('task_name', "default task name")
            task_description = task_data.get('task_description', "default task description")
            task_start_date = task_data.get('task_start_date', datetime.datetime.now())
            if task_start_date == '':
                task_start_date = datetime.datetime.now()
            task_end_date = task_data.get('task_end_date', datetime.datetime.now())
            if task_end_date == '':
                task_end_date = datetime.datetime.now()
            related_project_name = task_data.get('task_project_name', "default task description")
            project = Project.objects.get(name=related_project_name)
            task = Task(name=task_name, description=task_description, start_date=task_start_date,
                        end_date=task_end_date, project=project)
            task.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

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
        try:
            task_data = JSONParser().parse(request)
            task_name = task_data.get('task_name', "default task name")
            task_description = task_data.get('task_description', "default task description")
            task_start_date = task_data.get('task_start_date', datetime.datetime.now())
            if task_start_date == '':
                task_start_date = datetime.datetime.now()
            task_end_date = task_data.get('task_end_date', datetime.datetime.now())
            if task_end_date == '':
                task_end_date = datetime.datetime.now()
            related_project_name = task_data.get('task_project_name', "default task description")
            project = Project.objects.get(name=related_project_name)
            task.name = task_name
            task.description = task_description
            task.start_date = task_start_date
            task.end_date = task_end_date
            task.project = project
            task.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        task.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
