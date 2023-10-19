import django_filters
from django_filters import rest_framework as filters

from command_manager.models import Employee, Command, Project


class EmployeeFilter(filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr="icontains")
    position = filters.CharFilter(
        field_name="position__name",
        lookup_expr="iexact"
    )
    commands = filters.CharFilter(field_name="commands__name")

    class Meta:
        model = Employee
        fields = ["email", "position", "experience"]


class CommandFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    description = django_filters.CharFilter(lookup_expr="icontains")
    employees = django_filters.CharFilter(field_name="employees__email")

    class Meta:
        model = Command
        fields = ["name", "description", "employees"]


class ProjectFilter(filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr="icontains")
    commands = django_filters.CharFilter(field_name="commands__name")

    class Meta:
        model = Project
        fields = ["name", "commands", "budget", "deadline"]
