from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, "home.html")

def login(request):
    return render(request, "login.html")

@login_required
def profile(request, username):
    vars = {
        "username": username,
    }
    return render(request, "profile.html", vars)