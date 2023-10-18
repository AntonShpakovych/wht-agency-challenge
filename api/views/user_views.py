from rest_framework import generics

from api.serializers.user_serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
