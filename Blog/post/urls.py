from django.urls import path
from post.views import add_post

urlpatterns = [
    path('add/', add_post, name="add_post"),
]