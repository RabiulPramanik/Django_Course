from django.urls import path
from .views import add_post, edit_post, delete_post, PostCreateView, PostEditView, PostDeleteView, DetailPostView

urlpatterns = [
    # path('add_post/', add_post, name="postpage"),
    path('add_post/', PostCreateView.as_view(), name="postpage"),
    # path('add_post/edit/<int:id>', edit_post, name="editpage"),
    path('add_post/edit/<int:id>', PostEditView.as_view(), name="editpage"),
    # path('add_post/delete/<int:id>', delete_post, name="deletepage"),
    path('add_post/delete/<int:id>', PostDeleteView.as_view(), name="deletepage"),
    path('add_post/details/<int:id>', DetailPostView.as_view(), name="detailspage"),
]

