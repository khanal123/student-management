from django.urls import path
from .views import AllEvent, AddEvent, UpdateEvent, DeleteEvent

app_name = "event"

urlpatterns = [
    #event URL
    path("event/view/all/", AllEvent.as_view(), name='viewallevent'),
    path("new/event/add/", AddEvent.as_view(), name='addevent'),
    path("event/update/<int:pk>/", UpdateEvent.as_view(), name='updateevent'),
    path("event/delete/<int:pk>/", DeleteEvent.as_view(), name='deleteevent'),
]
