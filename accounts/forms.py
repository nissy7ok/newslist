from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from datetime import datetime

class SignUpForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(required=False)
    password2 = password1

    class Meta:
        model = User
        fields = ('username', 'password')