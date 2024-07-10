from django.urls import path
from .views import taskmodel, complete, edit, delete

urlpatterns = [
    path('', taskmodel, name="taskmodelpage"),
    path('complete/<int:id>', complete, name="complete"),
    path('edit/<int:id>',edit , name="edit"),
    path('delete/<int:id>',delete , name="delete"),
]