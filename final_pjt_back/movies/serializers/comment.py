from rest_framework import serializers
from ..models import Movie, Comment
from .user import UserSerializer


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class MovieListSerializer(serializers.ModelSerializer):
        class Meta:
            model = Movie
            fields = ('id', 'title', )
    Movie = MovieListSerializer(read_only=True)       
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('movie', 'user', 'username')