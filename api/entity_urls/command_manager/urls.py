from rest_framework import routers

from api.views.command_manager.views import (
    PositionViewSet,
    EmployeeViewSet,
    CommandViewSet,
    ProjectViewSet
)


command_manager_router = routers.DefaultRouter()

command_manager_router.register(
    "positions",
    PositionViewSet,
    basename="positions"
)
command_manager_router.register(
    "employees",
    EmployeeViewSet,
    basename="employees"
)
command_manager_router.register(
    "commands",
    CommandViewSet,
    basename="commands"
)
command_manager_router.register(
    "projects",
    ProjectViewSet,
    basename="projects"
)


command_manager_urlpatterns = [
    *command_manager_router.urls,
]
