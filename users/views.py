from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import RegisterSerializer, UserSerializer


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# get all users
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
