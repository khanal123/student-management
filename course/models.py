from django.db import models
from users.models import Student, Teacher

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Subjects(models.Model):
    name = models.CharField(max_length=200)
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CourseEnnrollment(models.Model):
    course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_id.name}-{self.student_id.full_name}"
    

class SubjectAsssign(models.Model):
    subject_id = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.subject_id.name}-{self.teacher_id.full_name}"
