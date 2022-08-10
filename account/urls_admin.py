from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import ListUserView, DetailedUserInfoView

app_name = 'admin_account'

urlpatterns = [
    # admin
    path('', ListUserView.as_view()),
    path('<str:username>/', DetailedUserInfoView.as_view()),
]
