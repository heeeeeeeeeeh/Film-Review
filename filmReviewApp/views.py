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
        "ads_news": models.Advertisement.objects.filter(section="news")
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
