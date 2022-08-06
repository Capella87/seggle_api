from django.contrib import admin
from django.urls import path, include
from .views import ListAnnouncements, AnnouncementDetailView

urlpatterns = [
    path('', ListAnnouncements.as_view(), name='list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='detailed_view')
]
