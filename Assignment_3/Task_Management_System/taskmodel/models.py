from django.db import models

class TaskModel(models.Model):
    title = models.CharField(max_length=200)
    decription = models.TextField()
    is_complete = models.BooleanField()
    assing_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.title
