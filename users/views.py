from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, TemplateView, ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# local import
from .models import CustomUser
from .forms import CustomLoginForm, SocialloginUserRoleForm
# Create your views here
    
# view for all user login
class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = CustomLoginForm
    
    def get_success_url(self):
        return reverse_lazy("course:homepage")
    

# view for social login
class SocialloginUserRole(UpdateView):
    model = CustomUser
    form_class = SocialloginUserRoleForm
    template_name = 'account/userrole.html'

    def get_success_url(self):
        return reverse_lazy('course:homepage')

    def get_object(self, queryset=None):
        return self.request.user

# view for user to selected how they want to register  
class ResgisterAsSelection(TemplateView):
    template_name = 'users/resgisterasselection.html'




    
