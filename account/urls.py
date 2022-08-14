from tokenize import Token
from django.urls import path
from django.urls import path, include
from django.contrib.auth import views as auth_views
from account.views import UserInfoView, SignUpView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    # User
    path('', SignUpView.as_view(), name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<str:username>/', UserInfoView.as_view(), name='detailed_view_for_admin'),
]
