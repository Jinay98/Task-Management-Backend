from django.db import models
#from tasks.models import Task


# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    duration = models.DateTimeField()
    #task = models.ForeignKey(Task, on_delete=models.CASCADE, blank=True, null=True)

    # image = models.ImageField(upload_to='project_image', blank=True)

    def __str__(self):
        return self.name
