from django.contrib import admin
from django.urls import path, include
from .views import ListAnnouncements, AnnouncementDetailView, AnnouncementCheckView

urlpatterns = [
    path('', ListAnnouncements.as_view(), name='list'),
    path('<int:pk>/', AnnouncementDetailView.as_view(), name='detailed_view'),
    path('<int:pk>/check/', AnnouncementCheckView.as_view(), name='update important/visible'),
]
