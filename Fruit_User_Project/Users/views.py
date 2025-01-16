from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer

@api_view(['GET','POST'])
def Show_Add_User(request):
    # an api call for getting all the users availabe and adding new ones
    pass


@api_view(['PUT','DELETE'])
def Update_User(request,id):
    # an api call for updating or deleting any user with a particular id
    pass