from rest_framework import generics

from drf_spectacular.utils import extend_schema

from api.serializers.user.serializers import UserSerializer


@extend_schema(tags=["User"])
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer
