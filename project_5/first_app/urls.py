from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('form/', views.from_input),
    path('django_form/', views.django_form),
    path('student_form/', views.passward_valid),
]