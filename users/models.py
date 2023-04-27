from django.contrib.auth.models import AbstractUser
from django.db import models

from first_try.models import Anime


class User(AbstractUser):
    image = models.ImageField(upload_to="static/vendor/users_images", null=True, blank=True,verbose_name="IMAGE URL")
    username = models.CharField(
        max_length=15,
        unique=True,)
    favorite_genres = models.CharField(max_length=200,null=True, blank=True)


    class Meta:
        verbose_name = "USER"
        verbose_name_plural = "USERS"
        ordering = ["username"]

class UserAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}'s anime list"
    
