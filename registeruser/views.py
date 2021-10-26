from django.shortcuts import render
from functools import partial
from rest_framework import serializers
from rest_framework.serializers import Serializer
from registeruser.serializers import AppUserSerializer
from django.shortcuts import render
from registeruser.models import AppUser
from django.http import HttpResponse,Http404,JsonResponse
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View 
from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from registeruser.models import AppUser
from registeruser.serializers import AppUserSerializer

class AppUserApi(APIView):
    print("AppuserApi")
    def post(self,request):
        print("Hello")
        print(request.data)
        serializer = AppUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("user created successfully")
            return Response("User created successfully",status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
    def get(self,request,email=None):
        if email is not None:
            try:
                user=AppUser.objects.get(email=email)
                serializer=AppUserSerializer(user)
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            except:
                return Response("Enter a valid email address",status=status.HTTP_400_BAD_REQUEST)
        else:
            user=AppUser.objects.all()
            serializer=AppUserSerializer(user,many=True)
            return Response(serializer.data,status=status.HTTP_201_CREATED)

# Create your views here.
