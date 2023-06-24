from django.contrib import admin
from .models import Course, Subjects, CourseEnnrollment, SubjectAsssign

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']

class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['name', 'course_id', 'created_at', 'updated_at']

admin.site.register(Course, CourseAdmin)
admin.site.register(Subjects, SubjectsAdmin)
admin.site.register(SubjectAsssign)
admin.site.register(CourseEnnrollment)