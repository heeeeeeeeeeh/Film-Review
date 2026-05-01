from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("newsletter/", views.newsletter_signup, name="newsletter"),
    path("moviesingle/", views.moviesingle, name="moviesingle"),
]
