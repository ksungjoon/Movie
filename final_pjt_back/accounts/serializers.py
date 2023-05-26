from rest_framework import serializers
from django.contrib.auth import get_user_model
# from movies.models import Movie
# from .models import Comment
# from movies.serializers import MovieListSerializer
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    # class MovieSerializer(serializers.ModelSerializer):
    #     class Meta:
    #         model = Movie
    #         fields = '__all__'

    # like_movies = MovieSerializer(many=True)

    class Meta:
        model = User
        fields = ('id','username','email','like_movies','watched_movies','followings','followers', 'profile_img')
        


class UserImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'like_movies', 'watched_movies', 'followings', 'followers', 'profile_img')
