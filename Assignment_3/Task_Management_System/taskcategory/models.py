from django.db import models
from taskmodel.models import TaskModel

class TaskCategory(models.Model):
    name = models.CharField(max_length=100)
    taskmodel = models.ManyToManyField(TaskModel)

    def __str__(self) -> str:
        return self.name
