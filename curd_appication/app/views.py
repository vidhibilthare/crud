from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password
from . models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    return render(request,"login.html")

def rajistration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if User.objects.filter(email = email).exists():
            messages.error(request,"Email is in Database")

        else:
            User.objects.create(name = name,email = email, password = password)
            return redirect("/login/")

