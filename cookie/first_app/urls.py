from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="homepage"),
    path('get/', views.get_cookie, name="getpage"),
    path('delete/', views.delete_cookie, name="deletepage"),
    path('set_session/', views.set_session, name="setsessionpage"),
    path('get_session/', views.get_session, name="getsessionpage"),
    path('del_session/', views.delete_session, name="delsessionpage"),
]