from django.db import models
from projects.models import Project


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
