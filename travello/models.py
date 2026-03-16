from django.db import models

# Create your models here.
class Destination(models.Model):
    # this is for DB models
    name = models.CharField(max_length=100)
    desc = models.TextField()
    reviews = models.TextField()
    days = models.TextField()
    offer = models.BooleanField()
    '''
    # this is for basic object creation to views file
    id : int
    name : str
    desc : str
    reviews : str
    days : str
    offer : bool
'''


