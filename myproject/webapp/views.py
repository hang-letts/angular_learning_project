from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import generics

from rest_framework.decorators import api_view

from .models import Employee
from .serealizers import EmployeeSerializer
from .models import Category
from .serealizers import CategorySerializer

# class EmployeeList(APIView):
#     def get(self, request):
#         employee1=Employee.objects.all()
#         serializer=EmployeeSerializer(employee1,many=True)
#         return Response(serializer.data)

class EmployeeList(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=CategorySerializer

# class CategoryList(APIView):
#     def get(self, request):
#         category1=Category.objects.all()
#         serializer=CategorySerializer(category1,many=True)
#         return Response(serializer.data)
class CategoryList(generics.ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

@api_view(['GET','POST'])
def category_list(request, format=None):
    # list of categories or update
    if request.method=='GET':
        categories=Category.objects.all()
        serializer=CategorySerializer(categories,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def category_detail(request,pk,format=None):
    #retrieve, update or delete
    try:
        category=Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=CategorySerializer(category)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer=CategorySerializer(category,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
