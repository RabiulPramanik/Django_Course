from django.urls import path
from .views import singup_user, login_user, logout_user

urlpatterns = [
    path('singup/', singup_user, name="singuppage"),
    path('login/', login_user, name="loginpage"),
    path('logout/',logout_user, name="logoutpage"),
]