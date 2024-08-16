from django.urls import path
from .views import add_profile, change_data, change_pass_with

urlpatterns = [
    path('add_profile/', add_profile, name="profilepage"),
    path('add_profile/<slug:category_slug>/', add_profile, name="profile_by_category_post"),
    path('add_profile/data_change/', change_data, name="datachange"),
    path('add_profile/pass_change_with/', change_pass_with, name="pass_change_with"),
]