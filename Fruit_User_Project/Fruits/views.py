# from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import Fruit
from .serializers import FruitSerializer

@api_view(['GET','POST'])
def Show_Add_Fruit(request):
    # an api call for getting all the fruits availabe and adding new ones
    pass


@api_view(['PUT','DELETE'])
def Update_Fruit(request,id):
    # an api call for updating or deleting any fruit with a particular id
    pass