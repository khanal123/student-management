from django.urls import path
from .views import AllNotice, AddNotice, UpdateNotice, DeleteNotice

app_name = "notice"

urlpatterns = [
    #notice URL
    path("notice/view/all/", AllNotice.as_view(), name='viewallnotice'),
    path("notice/add/", AddNotice.as_view(), name='addnotice'),
    path("notice/update/<int:pk>/", UpdateNotice.as_view(), name='updatenotice'),
    path("notice/delete/<int:pk>/", DeleteNotice.as_view(), name='deletenotice'),
]
