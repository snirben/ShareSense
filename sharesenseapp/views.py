# coding=utf-8
from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer, UsersSerializer, FireCamsSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
User = get_user_model()


class usersListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        users = User.objects.filter(role=0)
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class fireCamsListApiView(APIView):
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        users = User.objects.filter(role=0)
        serializer = FireCamsSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class whoIsInAPanicApiView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.filter(isPanic=True, role=0)
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
    id = int(request.data['id'])
    user = User.objects.get(id=id)
    userDistrict = user.district
    users = User.objects.filter(role=1, district=userDistrict)
    message = "אדם זקוק לעזרה בכתובת:   %s,%s, לעדכונך" % (user.address ,user.city)

    for user in users:
        send_mail(
            'התראת shareSense ',
            message,
            'sharesense2022@gmail.com',
            [user.email],
            fail_silently=False,
        )
    return Response(data={}, status=200)

@api_view(['POST'])
def togglePanic(request):
    print(request.data)
    user = User.objects.get(id=int(request.data['id']))
    layer = get_channel_layer()
    async_to_sync(layer.group_send)("update_users", {"type": "prep",})
    user.isPanic = not user.isPanic
    user.save()
    return Response(data={}, status=200)


@api_view(['POST'])
def toggleFire(request):
    user = User.objects.get(id=int(request.data['id']))
    user.isFire = not user.isFire
    layer = get_channel_layer()
    async_to_sync(layer.group_send)("update_users", {"type": "prep",})
    user.save()
    return Response(data={}, status=200)
