from django import template
from django.http import JsonResponse
from django.shortcuts import HttpResponse, render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse
from . import models
from .forms import LoginForm, NewsletterForm, SignupForm

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
        "signup_form": SignupForm(),
        "login_form": LoginForm(),
        "newsletter_form": NewsletterForm(),
    }
    template = loader.get_template("filmReviewApp/base.html")
    return HttpResponse(template.render(context, request))


def login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return JsonResponse({"redirected": "true", "url": reverse("index")})
        else:
            return JsonResponse({"errors": form.errors}, status=400)

    return JsonResponse({"error": "Invalid request method."}, status=400)


def signup(request):
    if request.method == "POST":
        form = SignupForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Account created successfully!"})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
        
    return JsonResponse({"error": "Invalid request method."}, status=400)


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
            return JsonResponse({"message": "Subscribed to newsletter!"})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
    return JsonResponse({"error": "Invalid request method."}, status=400)
