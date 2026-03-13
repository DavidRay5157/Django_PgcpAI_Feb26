from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from travello.models import *
# Create your views here.
def index(request):
    des1 = Destination()
    des1.name = "mumbai"
    des1.days = "20 days"
    des1.desc = "MumbaiKar"
    des1.reviews = "beautiful place"

    return render(request, 'index.html',{'des1':des1})