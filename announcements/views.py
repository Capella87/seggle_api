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
    permission_classes = [permissions.IsAdminUser, ]

    def get(self, request, pk):
        query = get_object_or_404(Announcement, pk=pk)
        serializer = AnnouncementSerializer(query)
        return Response(serializer.data)

    def put(self, request, pk):
        announcement = get_object_or_404(Announcement, pk=pk)
        data = request.data

        obje = {
            'title': data.get('title'),
            'description': data.get('description'),
            'is_visible': data.get('is_visible'),
            'is_important': data.get('is_important'),
            'writer': announcement.writer
        }
        serializer = AnnouncementSerializer(announcement, data=obje)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
    permission_classes = [permissions.IsAdminUser, ]

    def put(self, request, pk):
        query = get_object_or_404(Announcement, pk=pk)
        data = request.data
        obj = {
            "title": query.title,
            "description": query.description,
            "is_important": data.get('is_important'),
            "is_visible": data.get('is_visible'),
            "writer": query.writer,
        }
        serializer = AnnouncementSerializer(query, data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# For public users
class AnnouncementView(APIView):
    permission_classes = [permissions.IsAuthenticated, ]

    def get(self, request):
        target = Announcement.objects.filter(is_visible=True)
        serializer = AnnouncementSerializer(target, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
