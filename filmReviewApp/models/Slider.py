from django.db import models
from django.contrib.postgres.fields import ArrayField


class Slider(models.Model):
    image_src = models.CharField(max_length=200)
    image_width = models.IntegerField()
    image_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    movie_genre = ArrayField(models.CharField(max_length=10), blank=True, default=list)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)
