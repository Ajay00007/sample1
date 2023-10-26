from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import notes
# Create your views here.


def home(request):
    return render(request,'home.html')

def homescreen(request):
    return render(request,"homescreen.html")


def mappingscreen(request):
    return render(request,"mappingscreen.html")

def sqlscrappingmapping(request):
    return render(request,"sqlscrappingmapping.html")

def lineagepushscreen(request):  
    return render(request,"lineagepushscreen.html")

def Extract(request):
    return render(request,"Extract.html")

def mappingscreen(request):
    return render(request,"mappingscreen.html")

def sqlscrappingmapping(request):
    return render(request,"sqlscrappingmapping.html")

def lineagepushscreen(request):  
    return render(request,"lineagepushscreen.html")

def homescreen(request):
    return render(request,"homescreen.html")

def Extract(request):
    return render(request,"Extract.html")
