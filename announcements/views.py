from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, status
from .serializers import AnnouncementSerializer
from .models import Announcement

class ListAnnouncements(APIView):
    authentication_classes = [authentication.SessionAuthentication, authentication.TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated, ]

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

class AnnouncementEditor(APIView):
    #announcement 수정
    def put(self, request, pk):
        serializer = AnnouncementSerializer()###

        if pk.get('user_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            user_id = pk.get('user_id')
            update_user_serializer = serializer(user_id, data=request.data)###user_id가 아닌것같습니다
            if update_user_serializer.is_valid():
                update_user_serializer.save()
                return Response(update_user_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
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
