from django.urls import path
from .views import (Index, ViewAllSubject, AddSubjects, UpdateSubject, DeleteSubject, ViewAllCourse,
                     AddCourse, UpdateCourse, DeleteCourse, StudentCourseEnnrollment, AssignSubject)

app_name = "course"

urlpatterns = [
    path("", Index.as_view(), name="homepage"),

    #course URL
    path("course/view/all/", ViewAllCourse.as_view(), name='viewallcourse'),
    path("course/add/", AddCourse.as_view(), name='addcourse'),
    path("course/update/<int:pk>/", UpdateCourse.as_view(), name='updatecourse'),
    path("course/delete/<int:pk>/", DeleteCourse.as_view(), name='deletecourse'),

    #subjects URL
    path("subjects/view/all/", ViewAllSubject.as_view(), name='viewallsubject'),
    path("subjects/add/", AddSubjects.as_view(), name='addsubject'),
    path("subjects/update/<int:pk>/", UpdateSubject.as_view(), name='updatesubject'),
    path("subjects/delete/<int:pk>/", DeleteSubject.as_view(), name='deletesubject'),

    #assign URL
    path('teacher/subject/assign/', AssignSubject.as_view(), name="assignsubject"),

    #enroll URL
    path('student/course/enroll/', StudentCourseEnnrollment.as_view(), name="studentCourseennrollment"),
]
