from django.contrib.auth.models import AbstractUser
from django.db import models

from first_try.models import Anime


class User(AbstractUser):
    image = models.ImageField(upload_to="users_images", null=True, blank=True)

class UserAnime(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)