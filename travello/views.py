from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from travello.models import *
# Create your views here.
def index(request):
    '''
    # this is for manual data to show in index file
    des1 = Destination()
    des1.name = "mumbai"
    des1.days = "20 days"
    des1.desc = "MumbaiKar"
    des1.reviews = "beautiful place"
    des1.offer = True

    des2 = Destination()
    des2.name = "Kerela"
    des2.days = "10 days"
    des2.desc = "Gods own country"
    des2.reviews = "scenic place"
    des2.offer = True

    des3 = Destination()
    des3.name = "C-DAC"
    des3.days = "6 Months"
    des3.desc = "AI"
    des3.reviews = "Need Placement"
    des3.offer = False

    dest = [des1, des2, des3]
    '''

    dest = Destination.objects.all()

    return render(request, 'index.html',{'dest':dest})