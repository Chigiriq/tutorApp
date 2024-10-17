from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
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
    
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'
    context_object_name = 'user'

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(CustomUser, pk=pk)
