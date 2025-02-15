from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    birthdate = forms.DateField()

    class Meta:
        model = User
        fields = ['email', 'birthdate', 'password1', 'password2']