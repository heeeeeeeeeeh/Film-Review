from django.contrib import admin

from . import models

# Register your models here.
admin.site.register(models.Trailer)
admin.site.register(models.Slider)
admin.site.register(models.SocialLink)
admin.site.register(models.Genre)
admin.site.register(models.Advertisement)
admin.site.register(models.News)
admin.site.register(models.Tweet)