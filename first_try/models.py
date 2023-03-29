from django.db import models


class Anime(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5,decimal_places=1)
    episodes = models.PositiveIntegerField(null=True)
    duration = models.PositiveIntegerField(null=True)
    genres = models.TextField(null=True)
    images = models.ImageField(null=True)
    urls = models.URLField(null=True)

    def __str__(self):
        return self.name