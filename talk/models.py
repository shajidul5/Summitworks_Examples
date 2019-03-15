from django.db import models

# Create your models here.

class Talk(models.Model):
    name = models.CharField(max_length=100)
    speaker = models.CharField(max_length=100)
    venue = models.CharField(max_length=100)
    duration = models.DurationField()

