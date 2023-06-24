from django.urls import path
from .views import course_list, course_detail, subject_list, subject_detail

urlpatterns = [
    path('course/', course_list),
    path('course/<int:pk>/', course_detail),
    path('subject/', subject_list),
    path('subject/<int:pk>/', subject_detail),
]
