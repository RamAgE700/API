from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class MovieRecommendation(models.Model):
    genre = models.CharField(max_length=50, default='Unknown')  # Set a default value like 'Unknown'
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField()
    added_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)
    rating = models.IntegerField(null=True, blank=True)
    actors = models.CharField(max_length=255 ,null=True)

    def __str__(self):
        return f"{self.title} - Rated: {self.rating if self.rating is not None else 'Not Rated'}"
    
class Category(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name
