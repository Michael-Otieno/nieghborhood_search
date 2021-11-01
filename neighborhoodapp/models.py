from os import name
from django.db import models
from django.db.models import ImageField

# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    health_tel = models.IntegerField(null=True,blank=True)
    police_number = models.IntegerField(null=True,blank=True)
    family_count = models.IntegerField(null=True,blank=True)


