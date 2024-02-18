from django.db import models
from django import forms

class Profile (models.Model):
    email = models.EmailField(max_length=128)
    username = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30)
    password = models.CharField(max_length=50, widget=forms.PasswordInput)
