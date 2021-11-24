from django.db import models

# Create your models here.
class Tasks(models.Model):
    task_id = models.CharField(max_length=12)
    username = models.CharField(max_length=20)
    task = models.TextField()
    accomplished = models.BooleanField(default=False)