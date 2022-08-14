from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .serializers import AnnouncementSerializer
from .models import Announcement

class ListAnnouncements(APIView):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        queryset = Announcement.objects.all()
        serializer = AnnouncementSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        new_announcement = {
            'title': data['title'],
            'description': data['description'],
            'is_visible': data['is_visible'],
            'is_important': data['is_important'],
            'writer': request.user
        }
        serializer = AnnouncementSerializer(data=new_announcement)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class AnnouncementDetailView(APIView):

    queryset = Announcement.objects.all()
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request, pk):
        query = get_object_or_404(Announcement, pk=pk)
        serializer = AnnouncementSerializer(query)
        return Response(serializer.data)

    def delete(self, request, pk):
        target = get_object_or_404(Announcement, pk=pk)
        target.delete()
        return Response(status=status.HTTP_200_OK)

class AnnouncementCheckView(APIView):
    # 00-15 announcement_id인 announcement 수정 (important, visible)
    # 관리자만 접근 가능
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAdminUser, ]

    def put(self, request, pk):
        query = get_object_or_404(Announcement, pk=pk)
        data = request.data
        obj = {
            "title": query.title,
            "description": query.description,
            "important" : data["is_important"],
            "visible" : data["is_visible"]
        }
        serializer = AnnouncementSerializer(query, data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)