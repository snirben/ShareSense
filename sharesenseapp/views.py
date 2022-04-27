from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import MyTokenObtainPairSerializer,RegisterSerializer,UsersSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.core.mail import send_mail

User = get_user_model()


class usersListApiView(APIView):
    # add permission to check if user is authenticated
    #permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        users = User.objects.filter(role=0)
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

@api_view(['POST'])
def sendEmail(request):
    user= User.objects.get(id=2) 
    # id =request.user.id
    userDistrict= user.district
    users = User.objects.filter(role=1, district=userDistrict)
    for user in users:
        send_mail(
            'התראת shareSense ',
            'אדם זקוק לעזרה בכתובת: , לעדכונך',
            'sharesense2022@gmail.com',
            [user.email],
            fail_silently=False,
        )
    return Response(data={}, status=200)
