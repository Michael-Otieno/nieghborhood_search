from os import name
from django.db import models
from django.db.models import ImageField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class NeighbourHood(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='images/')
    description = models.TextField()
    health_tel = models.IntegerField(null=True,blank=True)
    police_number = models.IntegerField(null=True,blank=True)
    family_count = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return f'{self.name} hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=254, blank=True)
    profile_picture = models.ImageField

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=user)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
