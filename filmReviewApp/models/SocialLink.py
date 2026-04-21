from django.db import models


class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=2)
    icon_class = models.CharField(max_length=30)
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.name
