from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, TemplateView, ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

# local import
from .models import CustomUser, Student
from .forms import StudentSignUpForm, StudentProfileForm

# view for listing all student
class StudentList(ListView):
    model = Student
    paginate_by = 10
    context_object_name = 'students'
    template_name = 'users/student.html'

# view for student singup  
class StudentSignUpView(CreateView):
    model = CustomUser
    form_class = StudentSignUpForm
    template_name = 'users/signup.html'

    def form_valid(self, form):
        user =  form.save()
        login(self.request, user)
        return redirect("course:homepage")


# view for views the profile
class StudentProfile(DetailView):
    model = Student
    template_name = 'users/studentprofile.html'

    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(Student, user=UserName)


# view for student profile update   
class StudentUpdateprofile(UpdateView):
    model = Student
    form_class = StudentProfileForm
    
    template_name = 'users/studentprofile.html'

    def get_success_url(self):
        return reverse_lazy('course:homepage')