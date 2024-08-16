from django.urls import path
from . import views

urlpatterns = [
    path('details/<int:id>', views.car_details, name="detailspage"),
    # path('details/<int:id>', views.car_detailsView.as_view(), name="detailspage"),
]