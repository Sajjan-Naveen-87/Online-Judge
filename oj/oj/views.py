from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse

def firstPage(request):
    return render(request,'home/index.html') 