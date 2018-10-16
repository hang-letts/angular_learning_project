from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view

from .models import LoginModel, ProfileModel
from .serializers import LoginModelSerializer, ProfileModelSerializer

class LoginList(generics.ListAPIView):
    queryset=LoginModel.objects.all()
    serializer_class=LoginModelSerializer

#Login
@api_view(['GET','POST'])
def login_list(request, format=None):
    # list of categories or update
    if request.method=='GET':
        logins=LoginModel.objects.all()
        serializer=LoginModelSerializer(logins,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def login_detail(request,pk,format=None):
    #retrieve, update or delete
    try:
        login=LoginModel.objects.get(pk=pk)
    except LoginModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=LoginModelSerializer(login)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=LoginModelSerializer(login,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        login.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Profile
class AccountList(generics.ListAPIView):
    queryset=ProfileModel.objects.all()
    serializer_class=ProfileModelSerializer

#Profile
@api_view(['GET','POST'])
def account_list(request, format=None):
    # list of categories or update
    if request.method=='GET':
        accounts=ProfileModel.objects.all()
        serializer=ProfileModelSerializer(accounts,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=ProfileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def profile_detail(request,pk,format=None):
    #retrieve, update or delete
    try:
        profile=ProfileModel.objects.get(pk=pk)
    except ProfileModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=ProfileModelSerializer(profile)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=ProfileModelSerializer(profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
