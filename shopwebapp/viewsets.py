from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer
from . import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework import viewsets
from . import models

# Create your views here.
# Username (leave blank to use 'kalikali'): root
# Email address: prohuman001@gmail.com
# token


class ProductViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated] 
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
       