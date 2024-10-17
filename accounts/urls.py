from django.urls import path
from .views import SignUpView, UpdateHoursView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("add_hours/", UpdateHoursView.as_view(), name="add_hours"),
]