from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=64)
    anime_list = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.name

class Anime(models.Model):
    name = models.CharField(max_length=100)
    rating = models.DecimalField(max_digits=5,decimal_places=2)
    episodes = models.PositiveIntegerField()
    duration = models.PositiveIntegerField()
    genres = models.TextField()
    image = models.URLField()
    def __str__(self):
        return self.name