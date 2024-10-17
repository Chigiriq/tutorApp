from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm, UpdateHoursForm
from .models import CustomUser
from django.views.generic.edit import UpdateView

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = "registration/signup.html"
    
class UpdateHoursView(UpdateView):
    model = CustomUser
    form_class = UpdateHoursForm
    template_name = 'registration/add_hours.html'
    success_url = reverse_lazy('success')

    def get_object(self):
        return self.request.user