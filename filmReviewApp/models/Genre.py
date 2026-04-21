from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7)

    def __str__(self):
        return self.name
