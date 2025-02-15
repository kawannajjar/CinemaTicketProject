from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'birthdate']  # فیلدهایی که کاربر می‌تواند ویرایش کند
        
        
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    birthdate = forms.DateField()

    class Meta:
        model = User
        fields = ['email', 'birthdate', 'password1', 'password2']
