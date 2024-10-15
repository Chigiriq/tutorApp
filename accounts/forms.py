# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

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