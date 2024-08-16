from django.urls import path
from . import views

urlpatterns = [
    # path('singup/', views.singup_user, name="singuppage"),
    path('singup/', views.singupView.as_view(), name="singuppage"),
    # path('login/', views.login_user, name="loginpage"),
    path('login/', views.loginView.as_view(), name="loginpage"),
    # path('logout/', views.logout_user, name="logoutpage"),
    path('logout/', views.logoutView.as_view(), name="logoutpage"),
    path('profile/', views.profile, name="profilepage"),
    path('profile/edit/', views.profile_edit, name="profileEditPage"),
    path('changeData/', views.change_data, name="changeData"),
    path('changePassword/', views.change_pass_with, name="changePassword"),
    path('buyNow/<int:id>/', views.buyNow, name="buyNowpage")
]