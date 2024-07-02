from django.urls import path

from rest_framework.authtoken import views

from .views import RegisterCreateAPIView, UserListAPIView

# url register = /blog/api/users/register/

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
    path('users/', UserListAPIView.as_view()),
    path('login/', views.obtain_auth_token),
]
