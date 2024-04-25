from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import MovieRecommendation ,Category
from .serializers import MovieRecommendationSerializer, CategorySerializer
from django.views.generic import View
from django.http import HttpResponse

       

class movieViewset(generics.ListCreateAPIView):
    queryset = MovieRecommendation.objects.all()
    serializer_class= MovieRecommendationSerializer
    

class CategoryViewset(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class= CategorySerializer
    