from django.db import models

class News(models.Model):
    SECTION_CHOICES = [
        ('featured', 'Featured'),
        ('extra', 'Extra'),
    ]
    section = models.CharField(max_length=20, choices=SECTION_CHOICES)
    img_src = models.CharField(max_length=200, blank=True, default='')
    img_alt = models.CharField(max_length=100, blank=True, default='')
    img_width = models.IntegerField()
    img_height = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500, blank=True, default='')
    time = models.CharField(max_length=20)

    def __str__(self):
        return self.title