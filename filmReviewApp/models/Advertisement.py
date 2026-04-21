from django.db import models

class Advertisement(models.Model):
    SECTION_CHOICES = [
        ('movie', 'Movie'),
        ('news', 'News'),
    ]
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField()
    img_height = models.IntegerField()

    def __str__(self):
        return f"Ad - {self.section}"