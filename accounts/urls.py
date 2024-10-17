from django.urls import path
from .views import SignUpView, UpdateHoursView, user_list, UserProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("add_hours/", UpdateHoursView.as_view(), name="add_hours"),
    # path('users/', user_list, name='user_list'),
    path('user/<int:pk>/', UserProfileView.as_view(), name='user_profile'),
]