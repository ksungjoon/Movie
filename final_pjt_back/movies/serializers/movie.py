from rest_framework import serializers
from ..models import Movie, Genre, Comment
# from .user import UserSerializer

# class MovietitleSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Movie
#         fields = ('title',)

# class GenreSerializer(serializers.ModelSerializer):
#     # movies = MovietitleSerializer(many=True, read_only=True)
#     class Meta:
#         model = Genre
#         fields = '__all__'

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('id', 'name')


class MovieListSerializer(serializers.ModelSerializer):
    genres = GenreListSerializer(many=True, read_only=True, source='genre_ids')

    class Meta:
        model = Movie
        fields = ('id', 'title', 'release_date', 'popularity', 'vote_average', 'overview', 'poster_path', 'genres','liked_users')

