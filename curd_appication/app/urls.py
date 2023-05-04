from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login/", views.login),
    path("from/", views.rajistration),
    path("welcome/", views.welcome),
    path("login_user/", views.user_login),
    path("data/", views.data),

]
