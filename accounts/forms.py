# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("name", "classes", "hours")
        fields = (
            "username",
            "email",
            "name",
            "classes",
            "hours",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = fields = (
            "username",
            "email",
            "name",
            "classes",
            "hours",
        )

class UpdateHoursForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = (
            "hours",
        )

        # widgets = {
        #     'hours': forms.NumberInput(attrs={'min': 0}),
        # }