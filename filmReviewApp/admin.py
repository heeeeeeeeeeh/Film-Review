from django.contrib import admin
from .models import (
    Trailer,
    Slider,
    SocialLink,
    Genre,
    Advertisement,
    News,
    Tweet,
    Celebrity,
    MovieTheater,
    MovieTv,
)


# Register your models here.
admin.site.register(Trailer)
admin.site.register(Slider)
admin.site.register(SocialLink)
admin.site.register(Genre)
admin.site.register(Advertisement)
admin.site.register(MovieTv)
admin.site.register(MovieTheater)
admin.site.register(Celebrity)
admin.site.register(News)
admin.site.register(Tweet)
