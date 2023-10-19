from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),
    path(
        "api/v1/",
        include("api.urls", namespace="api")
    ),
    path(
        "api/v1/doc/",
        SpectacularAPIView.as_view(),
        name="schema"
    ),
    path(
        "api/v1/doc/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui"
    ),
    path(
        "__debug__/",
        include("debug_toolbar.urls")
    ),
]
