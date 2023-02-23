from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            "class":"inputs",
            "placeholder": "Введите имя",
            "required":""}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"inputs",
        "placeholder":"Введите пароль",
        "id":"password-input",
        "type":"password",
        "name":"password"}))

    class Meta:
        model = User
        fields = ("username", "password")

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "class":"inputs",
        "placeholder": "Введите ваш ник",}))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class":"inputs",
        "placeholder":"Введите имейл"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"inputs",
        "placeholder":"Введите пароль",
        "id":"password-input1",
        "type":"password",
        "name":"password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"inputs",
        "placeholder":"Повторите пароль",
        "id":"password-input2",
        "type":"password",
        "name":"password"}))
    
    class Meta:
        model = User
        fields = ("username", "email","password1","password2")