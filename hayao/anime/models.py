from django.db import models


# Create your models here.
class Anime(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    genre = models.CharField(max_length=256, blank=True)
    year = models.CharField(max_length=256)
    form = models.CharField(max_length=256)
    director = models.CharField(max_length=256, blank=True)
    screenwriter = models.CharField(max_length=256, blank=True)
    producer = models.CharField(max_length=256, blank=True)
    link = models.CharField(max_length=1024, blank=True)

    def __str__(self):
        return self.title
