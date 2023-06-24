from django import forms
from .models import Course, Subjects, SubjectAsssign, CourseEnnrollment

#form for the Course
class CourseForm(forms.ModelForm):
    name = forms.CharField(label="Enter Course name", widget=forms.TextInput(attrs={'placeholder': 'Enter Course name', 
                                                                                    'class':'form-control form-control-user'}))

    class Meta:
        model = Course
        fields = ['name']


# form for the Subjects
class SubjectsForm(forms.ModelForm):

    class Meta:
        model = Subjects
        fields = ['name', 'course_id']

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(SubjectsForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'




# form for the SubjectAssign
class SubjectAsssignForm(forms.ModelForm):

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(SubjectAsssignForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = SubjectAsssign
        fields = ['subject_id', 'teacher_id']


# form for CourseEnrollment
class CourseEnnrollmentForm(forms.ModelForm):

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(CourseEnnrollmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = CourseEnnrollment
        fields = ['course_id', 'student_id']

