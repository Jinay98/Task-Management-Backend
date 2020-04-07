from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
import datetime
from projects.models import Project
from projects.serializers import ProjectSerializer
from tasks.models import Task


@csrf_exempt
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        projects_serializer = ProjectSerializer(projects, many=True)
        return JsonResponse(projects_serializer.data, safe=False)

    elif request.method == 'POST':
        try:
            project_data = JSONParser().parse(request)
            name = project_data.get('name', 'default project name')
            description = project_data.get('description', 'default project description')

            duration = project_data.get('duration', datetime.datetime.now())
            if duration == '':
                duration = datetime.datetime.now()

            project = Project(name=name, description=description, duration=duration)
            project.save()
            return HttpResponse(status=status.HTTP_201_CREATED)


        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Project.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def project_detail(request, pk):
    try:
        project = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        project_serializer = ProjectSerializer(project)
        return JsonResponse(project_serializer.data)

    elif request.method == 'PUT':
        try:
            project_data = JSONParser().parse(request)
            name = project_data.get('name', 'updated project name')
            description = project_data.get('description', 'updated project description')

            duration = project_data.get('duration', datetime.datetime.now())
            if duration == '':
                duration = datetime.datetime.now()

            project.name = name
            project.description = description
            project.duration = duration
            project.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        except:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        project.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
