from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    adult = models.BooleanField(null=True)
    genre_ids = models.ManyToManyField(Genre, related_name='movies')
    original_language = models.CharField(max_length=100)
    original_title = models.CharField(max_length=100)
    overview = models.TextField()
    popularity = models.FloatField(null=True)
    poster_path = models.TextField()
    release_date = models.DateField(null=True)
    title = models.CharField(max_length=100)
    video = models.BooleanField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField(null=True)
    movie_id = models.IntegerField(null=True)
    liked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='like_movies')
    watched_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='watched_movies')
    
    
    

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
