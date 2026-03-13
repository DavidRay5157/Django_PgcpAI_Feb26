from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    #return HttpResponse("Hello, World!")
    return render(request, 'home.html',{'name' : 'mihir'})

def add(request):
    return render(request, "result.html", {'result' : 2})