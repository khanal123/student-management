from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import ResgisterAsSelection, UserLoginView
from .studentview import StudentSignUpView, StudentList, StudentProfile, StudentUpdateprofile
from .teacherview import TeacherList, TeacherSignUpView, TeacherProfileView, TeacherUpdateprofile

app_name="users"

urlpatterns = [
    # register selection url
    path("resgister/selection",ResgisterAsSelection.as_view(), name="resgisterselection"),

    # students urls
    path('student/signup', StudentSignUpView.as_view(), name="studentsignup"),
    path('student/list/all', StudentList.as_view(), name="studentlist"),
    path('student/profile/<int:username>/', StudentProfile.as_view(), name="studentprofile"),
    path('student/update/profile/<int:pk>/', StudentUpdateprofile.as_view(), name="studentupdateprofile"),

    # Teacher urls
    path('teacher/signup', TeacherSignUpView.as_view(), name="teachersignup"),
    path('teacher/list/all', TeacherList.as_view(), name="teacherlist"),
    path('teacher/profile/<int:username>/', TeacherProfileView.as_view(), name="teacherprofile"),
    path('teacher/update/profile/<int:pk>/', TeacherUpdateprofile.as_view(), name="teacherupdateprofile"),

    # login and logut urls
    path('logout/', LogoutView.as_view(next_page='course:homepage'), name='logout'),
    path('login/', UserLoginView.as_view(), name='login'),
]
