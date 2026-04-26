from . import models
from django.shortcuts import HttpResponse, render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    context = {
        "trailers": models.Trailer.objects.all(),
        "socials": models.SocialLink.objects.all(),
        "genres": {genre.name: genre.color for genre in models.Genre.objects.all()},
        "sliders": models.Slider.objects.all().order_by("id"),
        "ads_news": models.Advertisement.objects.filter(section="news"),
        "news_featured": models.News.objects.filter(section="featured").first(),
        "news_extra": models.News.objects.filter(section="extra"),
        "tweets": models.Tweet.objects.all(),
    }
    template = loader.get_template("filmReviewApp/base.html")
    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "Account created, login")
            return redirect("login")

    return render(request, "signup.html")


from .models import Celebrity, MovieTheater, MovieTv


def movielisting(request):
    context = {
        "celebrities": Celebrity.objects.all(),
        "theaters_popular": MovieTheater.objects.filter(type="popular"),
        "theaters_coming": MovieTheater.objects.filter(type="coming soon"),
        "tv_popular": MovieTv.objects.filter(type="popular"),
        "tv_coming": MovieTv.objects.filter(type="coming soon"),
    }
    return render(request, "filmReviewApp/movielist.html", context)


def moviesingle(request):
    template = loader.get_template("filmReviewApp/moviesingle.html")
    return HttpResponse(template.render({}, request))
