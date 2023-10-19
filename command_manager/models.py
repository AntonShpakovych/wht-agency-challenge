from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=20, unique=True)

    @property
    def employees_quantity(self) -> int:
        return self.employees.count()

    def __str__(self) -> str:
        return self.name


class Employee(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    experience = models.FloatField()
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        related_name="employees"
    )

    @property
    def commands_quantity(self) -> int:
        return self.commands.count()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name", "last_name"]


class Command(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    employees = models.ManyToManyField(Employee, related_name="commands")

    @property
    def command_size(self) -> int:
        return self.employees.count()

    @property
    def command_experience(self) -> float:
        return sum(
            employee.experience
            for employee in self.employees.all()
        )

    @property
    def projects_quantity(self) -> int:
        return self.projects.count()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Project(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    budget = models.DecimalField(max_digits=9, decimal_places=2)
    commands = models.ManyToManyField(Command, related_name="projects")
    deadline = models.DateField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]
