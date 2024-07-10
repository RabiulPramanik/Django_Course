from django.urls import path
from .views import taskcategory

urlpatterns = [
    path('', taskcategory, name="taskcategorypage"),
]