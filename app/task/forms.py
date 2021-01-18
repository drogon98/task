from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["name","email","phone","role","profile","password1","password2"]


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["name","email","phone","role","profile"]