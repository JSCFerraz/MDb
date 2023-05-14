from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsAllowedUser
from .models import User
from .serializers import UserSerializer
from rest_framework import generics


class UserView(generics.ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAllowedUser]

    queryset = User.objects.all()
    serializer_class = UserSerializer
