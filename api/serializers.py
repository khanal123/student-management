from rest_framework import serializers
from course.models import Course, Subjects

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'created_at', 'updated_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['name', 'course_id', 'created_at', 'updated_at']
