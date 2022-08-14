from django.contrib import admin
from django.urls import path, include
from .views import ListAnnouncements, AnnouncementDetailView, AnnouncementCheckView, AnnouncementView

urlpatterns = [
    path('', AnnouncementView.as_view(), name='for users')
]
