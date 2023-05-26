from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, UserImgSerializer
# from .models import Comment, Profile
from .models import User
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

@api_view(['GET'])
def user_profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
@api_view(['GET'])
def user_profile_id(request, id):
    user = get_object_or_404(get_user_model(), id=id)
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

# @api_view(['GET', 'PUT'])
# def upload_img(request, username):
#     user = get_object_or_404(get_user_model(), username=username)
#     print(user)
#     if request.method == 'GET':
#         serializer = UserImgSerializer(user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         if request.user != user:
#             return Response({'profile': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
#         serializer = UserImgSerializer(user, data=request.data, partial=True)
#         print(serializer)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             print('hi')
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
#     return Response({'profile': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def upload_img(request, username):
    user = get_object_or_404(User, username=username)
    print(user)
    if request.method == 'GET':
        serializer = UserImgSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        if request.user != user:
            return Response({'profile': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = UserImgSerializer(user, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            # 저장하기 전에 user.profile_img 필드에 데이터를 할당합니다.
            print(request.data)
            user.profile_img = request.data.get('image')
            print(user.profile_img)
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    return Response({'profile': '잘못된 요청입니다.'}, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def follow(request, username):
    user = get_object_or_404(User, username=username)
    if user !=  request.user:
        if user.followers.filter(pk=request.user.pk).exists():
            user.followers.remove(request.user)
        else:
            user.followers.add(request.user)       
    # context = {
    #     'followed' : followed,
    # }
    # return Response(context, status=status.HTTP_200_OK)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def follow_count(request, username):
    user = get_object_or_404(User, username=username)
    if user.followers.filter(pk=request.user.pk).exists():
        followed = True
    else:
        followed = False
    print(user)
    serializer= UserSerializer(user)
    print(len(serializer.data['followers']))
    if len(serializer.data['followers'])==0:
        followers_count = 0
    else:
        followers_count = len(serializer.data['followers'])
    if len(serializer.data['followings'])==0:
        followings_count = 0
    else:
        followings_count = len(serializer.data['followings'])
    data = {
        'followed':followed,
        'followers_count':followers_count,
        'followings_count':followings_count
    }
    return Response(data) 