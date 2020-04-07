from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=120, blank=False, default='')
    description = models.CharField(max_length=500, blank=False, default='')
    duration = models.DateTimeField()
    # TODO add an image field