from django.shortcuts import render, get_object_or_404
from rest_framework import status

from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import authentication
from rest_framework.pagination import PageNumberPagination

from .models import SeggleUser

from .serializers import UserSerializer, UserInfoSerializer, SignUpSerializer
from rest_framework.response import Response


# Views for Admin

class ListUserView(APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request, format=None):
        users = SeggleUser.objects.exclude(is_active=False)
        users = users.order_by('username')

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

class DetailedUserInfoView(APIView):
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request, username, format=None):
        user = get_object_or_404(SeggleUser, username=username)
        serializer = UserSerializer(user, many=False)

        return Response(serializer.data)

    # Kick the user
    def delete(self, request, username):
        violator = get_object_or_404(SeggleUser, username=username)

        if violator.is_active is False:
            return Response({'error': 'The user ' + violator.username + ' is already kicked or deleted.'})
        violator.is_active = False
        violator.save()
        return Response({'success': 'The user ' + violator.username + ' is successfully kicked.'},
                        status=status.HTTP_200_OK)
# Views for ordinary members

class SignUpView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            if request.data['password'] != request.data['password2']:
                data['error'] = 'Passwords must be matched.'
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            else:
                user = SeggleUser.objects.create(
                    username=request.data['username'],
                    email=request.data['email'],
                    name=request.data['name']
                )
                user.set_password(request.data['password'])
                user.save()

                data['response'] = user.name + ', Welcome to Seggle. You are now registered.'
                data['email'] = user.email
                data['username'] = user.username
                data['name'] = user.name
        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        return Response(data)

class UserInfoView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request, username, format=None):

        user = get_object_or_404(SeggleUser, username=username)
        serializer = UserInfoSerializer(user)

        return Response(serializer.data)
