from django.db import models


class Anime(models.Model):
    name = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=5,decimal_places=1)
    episodes = models.PositiveIntegerField(null=True)
    duration = models.PositiveIntegerField(null=True)
    genres = models.TextField(null=True)
    images = models.ImageField(upload_to="static/vendor/anime_images",null=True)
    urls = models.URLField(null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "ANIME"
        verbose_name_plural = "ANIMES"
        ordering = ["-rating","name"]