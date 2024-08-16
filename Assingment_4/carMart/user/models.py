from django.db import models
from car.models import CarModel
from django.contrib.auth.models import User

class ProfileModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ManyToManyField(CarModel)

