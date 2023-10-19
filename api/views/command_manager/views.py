from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from command_manager.models import (
    Position,
    Employee,
    Command,
    Project
)

from api.serializers.command_manager.serializers import (
    PositionSerializer,
    PositionListSerializer,
    PositionRetrieveSerializer,
    EmployeeSerializer,
    EmployeeListSerializer,
    EmployeeRetrieveSerializer,
    CommandSerializer,
    CommandListSerializer,
    CommandRetrieveSerializer,
    CommandAddSpecificEmployeeSerializer,
    CommandDeleteSpecificEmployeeSerializer,
    ProjectSerializer,
    ProjectListSerializer,
    ProjectRetrieveSerializer,
)
from api.paginations import (
    SmallResultsSetPagination,
    StandardResultsSetPagination
)

from api.filters.command_manager.filters import (
    EmployeeFilter,
    CommandFilter,
    ProjectFilter
)


@extend_schema(tags=["Position"])
class PositionViewSet(viewsets.ModelViewSet):
    model = Position
    pagination_class = SmallResultsSetPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return Position.objects.prefetch_related(
                "employees"
            )
        return Position.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PositionListSerializer
        elif self.action == "retrieve":
            return PositionRetrieveSerializer
        return PositionSerializer


@extend_schema(tags=["Employee"])
class EmployeeViewSet(viewsets.ModelViewSet):
    model = Employee
    pagination_class = StandardResultsSetPagination
    filterset_class = EmployeeFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action in ("list", "retrieve"):
            return Employee.objects.prefetch_related("commands")
        return Employee.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return EmployeeListSerializer
        elif self.action == "retrieve":
            return EmployeeRetrieveSerializer
        return EmployeeSerializer


@extend_schema(tags=["Command"])
class CommandViewSet(viewsets.ModelViewSet):
    model = Command
    pagination_class = StandardResultsSetPagination
    filterset_class = CommandFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action in (
                "list", "retrieve",
                "add_employee", "delete_employee"
        ):
            return Command.objects.prefetch_related("employees")
        return Command.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CommandListSerializer
        elif self.action == "retrieve":
            return CommandRetrieveSerializer
        elif self.action == "add_specific_employee":
            return CommandAddSpecificEmployeeSerializer
        elif self.action == "delete_specific_employee":
            return CommandDeleteSpecificEmployeeSerializer
        return CommandSerializer

    @action(
        detail=True,
        url_path="add-specific-employee",
        methods=["PATCH"],

    )
    def add_specific_employee(self, request, pk=None):
        command = self.get_object()
        serializer = self.get_serializer(
            data=request.data,
            context={"command": command}
        )

        if serializer.is_valid():
            serializer.update(
                instance=command,
                validated_data=serializer.validated_data
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=True,
        url_path="delete-specific-employee",
        methods=["PATCH"],

    )
    def delete_specific_employee(self, request, pk=None):
        command = self.get_object()
        serializer = self.get_serializer(
            data=request.data,
            context={"command": command}
        )

        if serializer.is_valid():
            serializer.update(
                instance=command,
                validated_data=serializer.validated_data
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@extend_schema(tags=["Project"])
class ProjectViewSet(viewsets.ModelViewSet):
    model = Project
    pagination_class = StandardResultsSetPagination
    filterset_class = ProjectFilter
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.action == "retrieve":
            return Project.objects.prefetch_related("commands")
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectListSerializer
        elif self.action == "retrieve":
            return ProjectRetrieveSerializer
        return ProjectSerializer
