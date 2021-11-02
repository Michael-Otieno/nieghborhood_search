from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django.forms import fields
from .models import Profile,NeighbourHood,Business,Post
from pyuploadcare.dj.forms import ImageField

class SignupForm(UserCreationForm):
    email=forms.EmailField(max_length=254, help_text='Requred.Inform a valid email address')
    class Meta:
        models=User
        fields=('username','email','password1','password2')

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=('user', 'neighbourhood')