from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/', views.user_profile, name='profile'),
    path('profile/id/<int:id>/', views.user_profile_id, name='profile_id'),
    path('<username>/follow/', views.follow, name='follow'),
    path('<username>/followcount/', views.follow_count, name='followcount'),
    path('upload_img/<username>/', views.upload_img, name='upload_img'),
] 
