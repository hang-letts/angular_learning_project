from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import LoginModel, ProfileModel
from .serializers import LoginModelSerializer, ProfileModelSerializer

#Login API        
class LoginAccountList(APIView):
    #Get all the login accounts
    def get(self, request, format=None):
        loginAccounts=LoginModel.objects.all()
        serializer=LoginModelSerializer(loginAccounts, many=True)
        return Response(serializer.data)
    
    #Create an login account
    def post(self, request, format=None):
        serializer=LoginModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Login Details view API
class LoginAccountDetail(APIView):
    #retrieve
    def get_object(self, pk):
        try:
            return LoginModel.objects.get(pk=pk)
        except LoginModel.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        loginAccount=self.get_object(pk)
        serializer=LoginModelSerializer(loginAccount)
        return Response(serializer.data)
    
    #PUSH: update login account
    def put(self, request, pk, format=None):
        loginAccount=self.get_object(pk)
        serializer=LoginModelSerializer(loginAccount, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk, format=None):
        loginAccount=self.get_object(pk)
        loginAccount.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Profile API        
class AccountList(APIView):
    #Get all the login accounts
    def get(self, request, format=None):
        accounts=ProfileModel.objects.all()
        serializer=ProfileModelSerializer(accounts, many=True)
        return Response(serializer.data)
    
    #Create an login account
    def post(self, request, format=None):
        serializer=ProfileModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Profile Details view API
class Profile(APIView):
    #retrieve
    def get_object(self, pk):
        try:
            return ProfileModel.objects.get(pk=pk)
        except ProfileModel.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        profile=self.get_object(pk)
        serializer=ProfileModelSerializer(profile)
        return Response(serializer.data)
    
    #PUSH: update login account
    def put(self, request, pk, format=None):
        profile=self.get_object(pk)
        serializer=ProfileModelSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #delete
    def delete(self, request, pk, format=None):
        profile=self.get_object(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)