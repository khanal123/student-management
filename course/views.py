from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView, FormView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


from users.models import CustomUser, Teacher, Student
from .models import Course, Subjects, SubjectAsssign, CourseEnnrollment
from .forms import SubjectsForm, CourseForm, SubjectAsssignForm, CourseEnnrollmentForm


# Create your views here.

# view for home page
class Index(LoginRequiredMixin,TemplateView):
    login_url = 'users:login'
    template_name = 'course/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_student"] = CustomUser.objects.filter(user_role="Student").count()
        context["total_teacher"] = CustomUser.objects.filter(user_role="Teacher").count()
        context["total_course"] = Course.objects.count()
        context["total_subject"] = Subjects.objects.count()
        context["teacher"] = Teacher.objects.filter(user=self.request.user)
        context["student"] = Student.objects.filter(user=self.request.user)
        return context
    

#Start of Course view

# view for listing all course
class ViewAllCourse(ListView):
    model = Course
    paginate_by = 4
    context_object_name = 'course'
    template_name = 'course/course.html'

# view for adding course  
class AddCourse(PermissionRequiredMixin ,CreateView):
    permission_required = "course.can_add_course"
    model = Course    
    form_class = CourseForm
    template_name = 'course/addcourse.html'

    def get_success_url(self):
        return reverse_lazy("course:viewallcourse")


# view for updating course  
class UpdateCourse(PermissionRequiredMixin, UpdateView):
    permission_required = "course.can_change_course"
    model = Course
    form_class = CourseForm
    template_name = 'course/updatecourse.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy("course:viewallcourse")

# view for deleting Course   
class DeleteCourse(PermissionRequiredMixin, DeleteView):
    permission_required = "course.can_delete_course"
    model = Course
    template_name = 'course/deletecourse.html'
    def get_success_url(self):
        return reverse_lazy("course:viewallcourse")
    
#End of course View



# start of subject view 

# view for listing all subjects 
class ViewAllSubject(ListView):
    model = Subjects
    paginate_by = 5
    context_object_name = 'subjects'
    template_name = 'course/subject.html'


# view for adding subject  
class AddSubjects(PermissionRequiredMixin, CreateView):
    permission_required = 'course.can_add_subjects'
    model = Subjects   
    form_class = SubjectsForm
    template_name = 'course/addsubject.html'

    def get_success_url(self):
        return reverse_lazy("course:viewallsubject")


# view for updating subjects   
class UpdateSubject(PermissionRequiredMixin, UpdateView):
    permission_required = 'course.can_edit_the_subjects'
    model = Subjects
    form_class = SubjectsForm
    template_name = 'course/updatesubject.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy("course:viewallsubject")
    

# view for deleting subjects  
class DeleteSubject(PermissionRequiredMixin, DeleteView):
    permission_required = 'course.can_delete_subjects'
    model = Subjects
    template_name = 'course/deletesubject.html'

    def get_success_url(self):
        return reverse_lazy("course:viewallsubject")
    
# end of subject view   


# Start of subject Assign

# view for assigning subjects to the teacher
class AssignSubject(PermissionRequiredMixin, CreateView):
    permission_required = 'course.can_add_subject_assign'
    model = SubjectAsssign
    form_class = SubjectAsssignForm
    template_name = "course/assignsubject.html"

    def get_success_url(self):
        return reverse_lazy("course:")
    

# End of subject Assign


# Start of Course Ennrollment

# view for enrolling student to course
class StudentCourseEnnrollment(PermissionRequiredMixin, CreateView):
    permission_required = 'course.can_add_subjects_course_enrollment'
    model = CourseEnnrollment
    form_class = CourseEnnrollmentForm
    template_name = "course/courseennrollment.html"

    def get_success_url(self):
        return reverse_lazy("course:")

# End of Course Ennrollment