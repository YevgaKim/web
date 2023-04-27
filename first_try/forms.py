from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.forms import Form

from users.models import User


class UserProfileForm(UserChangeForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={"id":"file-input",
        "name":"photo",
        "accept":"image/*",}))
    class Meta:
        model = User
        fields = ("image",)
