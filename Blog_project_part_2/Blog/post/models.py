from django.db import models
from django.contrib.auth.models import User
from category.models import CategoryModel

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    contant = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self) -> str:
        return self.title
