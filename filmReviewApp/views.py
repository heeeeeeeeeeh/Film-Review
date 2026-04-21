from . import models
from django.shortcuts import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    context = {
        "trailers": models.Trailer.objects.all(),
        "socials": models.SocialLink.objects.all(),
        "genres": {genre.name: genre.color for genre in models.Genre.objects.all()},
        "sliders": models.Slider.objects.all().order_by("id"),
    }
    template = loader.get_template("filmReviewApp/base.html")
    return HttpResponse(template.render(context, request))
