from django.db import models
from brand.models import BrandModel

class CarModel(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.name} of {self.brand.name}'
