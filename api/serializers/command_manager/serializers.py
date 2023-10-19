from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from command_manager.models import (
    Position,
    Employee,
    Command,
    Project
)


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ["id", "name"]


class PositionListSerializer(PositionSerializer):
    class Meta(PositionSerializer.Meta):
        fields = PositionSerializer.Meta.fields + ["employees_quantity"]


class PositionRetrieveSerializer(PositionSerializer):
    class Meta(PositionSerializer.Meta):
        fields = PositionSerializer.Meta.fields + ["employees"]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            "id", "email", "first_name",
            "last_name", "experience", "position"
        ]


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "email", "commands_quantity"]


class EmployeeRetrieveSerializer(EmployeeSerializer):
    class Meta(EmployeeSerializer.Meta):
        fields = EmployeeSerializer.Meta.fields + ["commands"]


class CommandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ["id", "name", "description", "employees"]


class CommandListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = [
            "id", "name", "description",
            "command_size", "command_experience",
            "projects_quantity"
        ]


class CommandRetrieveSerializer(serializers.ModelSerializer):
    employees = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="email"
    )
    projects = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Command
        fields = [
            "id", "name", "description",
            "employees", "projects"
        ]


class CommandAddSpecificEmployeeSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()

    def validate_employee_id(self, value):
        employee = Employee.objects.filter(id=value)

        if not employee:
            raise ValidationError(
                "Employee with such ID is not found"
            )
        elif employee.first() in self.context["command"].employees.all():
            raise ValidationError(
                "Employee with such ID already exists in this command"
            )
        return value

    def update(self, instance, validated_data):
        employee = Employee.objects.get(id=validated_data.get("employee_id"))
        instance.employees.add(employee)
        instance.save()

        return instance


class CommandDeleteSpecificEmployeeSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()

    def validate_employee_id(self, value):
        employee = Employee.objects.filter(id=value)

        if not employee:
            raise ValidationError(
                "Employee with such ID is not found"
            )
        if employee.first() not in self.context["command"].employees.all():
            raise ValidationError(
                "There is no worker with such an ID in the team"
            )
        return value

    def update(self, instance, validated_data):
        employee = Employee.objects.get(id=validated_data.get("employee_id"))

        instance.employees.remove(employee)
        instance.save()

        return instance


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "id", "name", "description",
            "budget", "commands", "deadline"
        ]


class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "deadline"]


class ProjectRetrieveSerializer(ProjectSerializer):
    commands = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )
