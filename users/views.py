from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.exceptions import PermissionDenied

from rest_framework.permissions import IsAuthenticated

from .serializers import RegisterSerializer, UserSerializer

class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# get all users
class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


# only admin can be see all users
    def get_queryset(self):
        if self.request.user.is_staff:
            return super().get_queryset()
        else:
            raise PermissionDenied("You do not have permission to access the requested data only admin")  
