from django.db import models
from car.models import CarModel

class CommentModel(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE)
