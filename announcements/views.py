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