import imp
from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=80)
    family = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    age = models.IntegerField()

    def __str__(self):
        return self.name