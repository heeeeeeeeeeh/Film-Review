from django.db import models

class Celebrity(models.Model):
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    anchor_url = models.CharField(max_length=200)
    celebrity_name = models.CharField(max_length=50)
    celebrity_url = models.CharField(max_length=200)
    celebrity_type = models.CharField(max_length=20)

    def __str__(self):
        return self.celebrity_name