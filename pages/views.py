from django.shortcuts import render
from django.views.generic import TemplateView
from accounts.models import CustomUser

class HomePageView(TemplateView):
    template_name = "home.html"
    model = CustomUser
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = CustomUser.objects.all()
        
        print(users)
        print(f"Users in context: {list(users)}")
        
        context['users'] = users
        return context

    