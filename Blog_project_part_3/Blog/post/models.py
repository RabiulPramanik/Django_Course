from django.db import models
from django.contrib.auth.models import User
from category.models import CategoryModel

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    contant = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(CategoryModel)
    image = models.ImageField(upload_to ='uploads/', blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class CommentModel(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=30)
    email = models.EmailField()
    body = models.TextField()
    create_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
