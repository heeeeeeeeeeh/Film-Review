from django.shortcuts import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    context = {}
    template = loader.get_template("filmReviewApp/base.html")
    return HttpResponse(template.render(context, request))
