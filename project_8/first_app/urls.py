from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('singup/', views.singup, name="singuppage"),
    path('login/', views.user_login, name="loginpage"),
    path('profile/', views.profile, name="profilepage"),
    path('logout/', views.user_logout, name="logoutpage"),
    path('passchange/', views.pass_Change, name="passchangepage"),
    path('passchange2/', views.pass_Change2, name="passchange2page"),
    path('datachange/', views.datachange, name="datachangepage"),
]