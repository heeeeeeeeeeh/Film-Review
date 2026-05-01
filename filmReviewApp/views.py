from django import template
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from . import models
from .forms import NewsletterForm

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
        "celebrities": models.Celebrity.objects.all(),
        "theaters_popular": models.MovieTheater.objects.filter(type="Popular"),
        "theaters_coming": models.MovieTheater.objects.filter(type="Coming Soon"),
        "tv_popular": models.MovieTv.objects.filter(type="Popular"),
        "tv_coming": models.MovieTv.objects.filter(type="Coming Soon"),
        "ads": models.Advertisement.objects.filter(section="movie"),
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

    return render(request, "filmReviewApp/login.html")


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
        
    return render(request, "filmReviewApp/signup.html")


def movielisting(request):
    context = {
        "celebrities": Celebrity.objects.all(),
        "theaters_popular": MovieTheater.objects.filter(type="Popular"),
        "theaters_coming": MovieTheater.objects.filter(type="Coming soon"),
        "tv_popular": MovieTv.objects.filter(type="Popular"),
        "tv_coming": MovieTv.objects.filter(type="Coming soon"),
        "ads": Advertisement.objects.filter(section="movie"),
    }
    return render(request, "filmReviewApp/movielist.html", context)


def moviesingle(request):
    template = loader.get_template("filmReviewApp/moviesingle.html")
    return HttpResponse(template.render({}, request))

def newsletter_signup(request):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Subscribed to newsletter!")
            return JsonResponse({"message": "Subscribed to newsletter!"})
        else:
            messages.error(request, "Invalid email address.")
            return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=400)
