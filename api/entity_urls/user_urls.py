from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from api.views.user_views import UserCreateView


user_urlpatterns = [
    path(
        "user/create/",
        UserCreateView.as_view(),
        name="user-create"
    ),
    path(
        "user/token/",
        TokenObtainPairView.as_view(),
        name="token_obtain_pair"
    ),
    path(
        "user/token/refresh/",
        TokenRefreshView.as_view(),
        name="token_refresh"
    ),
    path(
        "user/token/verify/",
        TokenVerifyView.as_view(),
        name="token_verify"
    )
]