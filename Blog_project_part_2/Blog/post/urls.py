from django.urls import path
from .views import add_post, edit_post, delete_post

urlpatterns = [
    path('add_post/', add_post, name="postpage"),
    path('add_post/edit/<int:id>', edit_post, name="editpage"),
    path('add_post/delete/<int:id>', delete_post, name="deletepage"),
]