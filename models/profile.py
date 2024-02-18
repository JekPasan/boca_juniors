from django.db import models
from django import forms

class Profile (models.Model):
    email = models.EmailField(max_length=128)
    username = models.CharField(max_length=30, min_length=3)
    nickname = models.CharField(max_length=30, min_length=3)
    password = models.CharField(max_length=50, min_length=6, widget=forms.PasswordInput)
