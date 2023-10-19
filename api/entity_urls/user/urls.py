from django.urls import path
from drf_spectacular.utils import extend_schema

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api.views.user.views import UserCreateView


user_urlpatterns = [
    path(
        "user/create/",
        UserCreateView.as_view(),
        name="user-create"
    ),
    path(
        "user/token/",
        extend_schema(tags=["User"])(TokenObtainPairView).as_view(),
        name="token_obtain_pair"
    ),
    path(
        "user/token/refresh/",
        extend_schema(tags=["User"])(TokenRefreshView).as_view(),
        name="token_refresh"
    ),
    path(
        "user/token/verify/",
        extend_schema(tags=["User"])(TokenVerifyView).as_view(),
        name="token_verify"
    )
]
