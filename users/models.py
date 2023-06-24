from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USERS_roles = (
        ("Principal", "Principal"),
        ("Teacher", "Teacher"),
        ("Student", "Student")
    )
    user_role = models.CharField(choices=USERS_roles, default="Student", max_length=10)

class Teacher(models.Model):
    Gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others','Others')
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=Gender_choice, null=True)
    image = models.ImageField(upload_to='images/profile/teachers/%Y/%m/%d/', null=True)
    address = models.CharField(max_length=200, null=True)
    experience = models.IntegerField(null=True)
    degree = models.CharField(max_length=50, null=True)
    phone_no = models.CharField(verbose_name="phone number", max_length=15, null=True)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username
    

class SessionYearModel(models.Model):
    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()

    def __str__(self):
        return f'{self.session_start_year}-{self.session_end_year}'
    

class Student(models.Model):
    Gender_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others','Others')
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=250, null=True)
    birth_date = models.DateField(null=True)
    gender = models.CharField(max_length=10, choices=Gender_choice, null=True)
    image = models.ImageField(upload_to='images/profile/students/%Y/%m/%d/', null=True)
    address = models.CharField(max_length=200, null=True)
    session_year_id = models.ForeignKey(SessionYearModel, on_delete=models.CASCADE,  null=True)
    phone_no = models.CharField(verbose_name="phone number", max_length=15, null=True)
    joined_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.user.username