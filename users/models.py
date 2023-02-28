from django.contrib.auth.models import AbstractUser
from django.db import models

from first_try.models import Anime


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)

class UserAnime(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='anime_list')
    anime = models.ManyToManyField(Anime, blank=True, related_name='users')

    def __str__(self):
        return f"{self.user.username}'s anime list"