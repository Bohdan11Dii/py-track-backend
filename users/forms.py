from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import CustomUser


class UserRegistration(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")

        help_texts = {
            'username': None,
        }
