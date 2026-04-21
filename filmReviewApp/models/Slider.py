from django.db import models
from .Genre import Genre


class Slider(models.Model):
    image_src = models.CharField(max_length=200)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genres = models.ManyToManyField(Genre, related_name="sliders", blank=True)

    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)
