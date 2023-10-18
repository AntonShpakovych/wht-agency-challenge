from api.entity_urls import user_urls


urlpatterns = [
    *user_urls.user_urlpatterns
]

app_name = "api"
