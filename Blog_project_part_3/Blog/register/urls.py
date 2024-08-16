from django.urls import path
from .views import singup_user, login_user, logout_user, login_user_view, logout_user_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('singup/', singup_user, name="singuppage"),
    # path('login/', login_user, name="loginpage"),
    path('login/', login_user_view.as_view(), name="loginpage"),
    path('logout/',logout_user, name="logoutpage"),
    # path('logout/',logout_user_view.as_view(), name="logoutpage"),
]