
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('genres/', views.genrelist),
    path('comments/list/<int:movie_pk>/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('movies/<int:movie_pk>/comments/', views.comment_create),
    path('movies/<int:movie_id>/like/', views.like_movie),
    path('movies/<int:movie_id>/like/count', views.like_movie_users),
    path('movies/<int:movie_id>/watched/', views.watched_movie),
    path('movies/<int:movie_id>/watched/count', views.watched_movie_users)
]
