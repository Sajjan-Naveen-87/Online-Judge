from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home/home.html')

def login(request):
    return HttpResponse('Login Page')

def logout(request):
    return render(request,'home/index.html')

def createGroup(request):
    return render(request,'home/createGroup.html')

def joinGroup(request):
    return render(request,'home/joinGroup.html')

def practice(request):
    return render(request,'home/practice.html')