from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
    password_confirmation = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email is already in use.")
        return email


class LoginForm(forms.Form):
    username_or_email = forms.CharField(max_length=254)
    password = forms.CharField(
        max_length=150,
        widget=forms.PasswordInput,
    )
