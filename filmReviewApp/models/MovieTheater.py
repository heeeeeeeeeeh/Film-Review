from django.db import models

class MovieTheater(models.Model):
    type = models.CharField(max_length=20)
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    img_src = models.CharField(max_length=200)
    anchor_url = models.CharField(max_length=200)
    lower_rating = models.CharField(max_length=5)
    upper_rating = models.CharField(max_length=5)
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)

    def __str__(self):
        return self.movie_title
    
