from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models import *
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


def login(request):
    return render(request, "login.html")


def welcome(request):
    return render(request, "welcome.html")


def data(request):
    tabble_obj = User.objects.all()
    return render(request,'table.html',{'table_obj':tabble_obj})

def user_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        user_password=request.POST['password']
        if User.objects.filter(email = email).exists():
            obj = User.objects.get(email = email)
            password = obj.password
            if check_password(user_password,password):
                return redirect('/data/')
            else:
                return HttpResponse('password incorrect')
    else:
        return HttpResponse('Email is not rajister')

def rajistration(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        password = make_password(request.POST["password"])
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email is in Database")

        else:
            User.objects.create(name=name, email=email, password=password)
            return redirect("/login/")
