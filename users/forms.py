from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import Group
from django import forms

from .models import CustomUser, Student, Teacher

# custom user creatioin form for admin
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ['username',]

# custom user change form for admin
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username',]

# student singup form
class StudentSignUpForm(UserCreationForm):
    username = forms.CharField(label="Enter username", widget=forms.TextInput(attrs={'placeholder': 'Username', 
                                                                                    'class':'form-control form-control-user'}))
    
    email = forms.EmailField(label="Enter Email", widget=forms.EmailInput(attrs={'placeholder': 'Email', 
                                                                                    'class':'form-control form-control-user'}))
    
    password1 = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 
                                                                                    'class':'form-control form-control-user'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 
    
                                                                                    'class':'form-control form-control-user'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.user_role = "Student"
        user.save()
        return user

# Teacher singup form
class TeacherSignUpForm(UserCreationForm):
    username = forms.CharField(label="Enter username", widget=forms.TextInput(attrs={'placeholder': 'Username', 
                                                                                    'class':'form-control form-control-user'}))
    
    email = forms.EmailField(label="Enter Email", widget=forms.EmailInput(attrs={'placeholder': 'Email', 
                                                                                    'class':'form-control form-control-user'}))
    
    password1 = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 
                                                                                    'class':'form-control form-control-user'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password', 
                                                                                    'class':'form-control form-control-user'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, *args, **kwargs):
        user = super().save(commit=False)
        user.user_role = "Teacher"
        user.save()
        return user
    
# Login form
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label="Enter username", widget=forms.TextInput(attrs={'placeholder': 'Username', 
                                                                                    'class':'form-control form-control-user'}))
    password = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder': 'Password', 
                                                                                    'class':'form-control form-control-user'}))
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


# social login form
class SocialloginUserRoleForm(forms.ModelForm):
    USERS_roles = (
        ("Teacher", "Teacher"),
        ("Student", "Student")
    )
    user_role = forms.ChoiceField(choices=USERS_roles)
    class Meta:
        model = CustomUser
        fields = ['user_role']

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(SocialloginUserRoleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# student profile form
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'birth_date', 'gender', 'image', 'address', 'session_year_id', 'phone_no']

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


# teacher Profile form
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'birth_date', 'gender', 'image', 'address', 'degree', 'experience', 'phone_no']

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(TeacherProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

