from django.urls import path
from users.views import RegisterAPIView, UserListAPIView, ProfileAPIView, UserListView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='api_register'),
    path('users/', UserListAPIView.as_view(), name='api_user_list'),
    path('profile/', ProfileAPIView.as_view(), name='api_profile'),
    path('userlist/', UserListView.as_view(), name='user_list'),
]