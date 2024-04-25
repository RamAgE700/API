from django.urls import path
from . import views

urlpatterns = [
    path('',views.movieViewset.as_view(), name='movie-recommendations'),
    path('cat',views.CategoryViewset.as_view(), name='Category'),
]