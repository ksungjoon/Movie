from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Movie, Comment, Genre
from .serializers.movie import MovieListSerializer, GenreListSerializer
from .serializers.comment import CommentSerializer 

# Create your views here.
@api_view(['GET'])

def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])

def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    user = request.user
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if user.pk == comment.user_id:    
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    
@api_view(['GET'])
def comment_list(request, movie_pk):
    if request.method == 'GET':
        movie = get_object_or_404(Movie, pk=movie_pk)
        # comments = Comment.objects.all()
        comments = Comment.objects.filter(movie=movie)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def comment_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
@api_view(['GET'])
def genrelist(request):
    genres = Genre.objects.all()
    serializer = GenreListSerializer(genres, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def like_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    user = request.user

    if user in movie.liked_users.all():
        movie.liked_users.remove(user)        
    else:
        movie.liked_users.add(user)
    serializer = MovieListSerializer(movie)
    data = {
        'movie': serializer.data,
    }
    return Response(data)

@api_view(['GET'])
def like_movie_users(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(id=movie_id)
        user = request.user     
        if user in movie.liked_users.all():
            liked = True
        else:
            liked = False
        print(movie.liked_users.count())
        if movie.liked_users.count() == 0:
            likes_count = 0
        else:
            likes_count = movie.liked_users.count()

        data ={
            'liked': liked,
            'likes_count': likes_count,
        }
        return Response(data)
    
@api_view(['POST'])
def watched_movie(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    user = request.user

    if user in movie.watched_users.all():
        movie.watched_users.remove(user)        
    else:
        movie.watched_users.add(user)
    serializer = MovieListSerializer(movie)
    data = {
        'movie': serializer.data,
    }
    return Response(data)

@api_view(['GET'])
def watched_movie_users(request, movie_id):
    if request.method == 'GET':
        movie = Movie.objects.get(id=movie_id)
        user = request.user     
        if user in movie.watched_users.all():
            watched = True
        else:
            watched = False

        data ={
            'watched': watched,
        }
        return Response(data)