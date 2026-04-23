from django.urls import path
from . import views

urlpatterns = [path("", views.index, name="index"),
               path("login/", views.login, name="login"),
               path("signup/", views.signup, name="signup"),
               path("movielist/", views.movielisting, name="movielist"),
               path("moviesingle/<int:id>/", views.movesingle, name="movesingle")
               ]
