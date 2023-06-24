from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

# local import
from .models import CustomUser, Teacher
from .forms import TeacherSignUpForm, TeacherProfileForm

# view for tescher signup
class TeacherSignUpView(CreateView):
    model = CustomUser
    form_class = TeacherSignUpForm
    template_name = 'users/signup.html'
    
    def get_success_url(self):
        return reverse_lazy("course:homepage")
    
# view for listing all teacher
class TeacherList(ListView):
    model = Teacher
    paginate_by = 10
    context_object_name = 'teachers'
    template_name = 'users/teacher.html'

# view for viewing teacher profile
class TeacherProfileView(DetailView):
    model = Teacher
    context_object_name = 'teacher'
    template_name = 'users/teacherprofile.html'

    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(Teacher, user=UserName)
    

# view for teacher profile update
class TeacherUpdateprofile(UpdateView):
    model = Teacher
    form_class = TeacherProfileForm
    template_name = 'users/profileupdate.html'

    def get_success_url(self):
        return reverse_lazy("course:homepage")

