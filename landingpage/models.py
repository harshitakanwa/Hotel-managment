from django.db import models

# Create your models here.
class Queries(models.Model):
    email =  models.TextField()
    query = models.TextField()