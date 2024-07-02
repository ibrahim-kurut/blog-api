from django.urls import path

from .views import RegisterCreateAPIView

# url register = /blog/api/users/register/

urlpatterns = [
    path('register/', RegisterCreateAPIView.as_view()),
]
