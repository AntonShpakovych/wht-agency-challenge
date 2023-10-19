from api.entity_urls.user.urls import user_urlpatterns
from api.entity_urls.command_manager.urls import command_manager_urlpatterns


urlpatterns = [
    *user_urlpatterns,
    *command_manager_urlpatterns
]

app_name = "api"
