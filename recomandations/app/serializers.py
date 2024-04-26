
from rest_framework import serializers
from .models import MovieRecommendation,  Category
from django.contrib.auth.models import User

class MovieRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRecommendation
        fields = ['id', 'title', 'description', 'release_date', 'image','added_on', 'rating','genre','actors' ]
   
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name',]


