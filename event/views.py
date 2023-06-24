from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Event, EventPrticipant
from .forms import EventForm

# Create your views here.

# view for listing all event
class AllEvent(ListView):
    model = Event
    context_object_name = 'events'
    template_name = 'event/event.html'


# view for adding event
class AddEvent(PermissionRequiredMixin, CreateView):
    permission_required = 'notice.can_view_add_remove_event'
    model = Event    
    form_class = EventForm
    template_name = 'event/addevent.html'

    def get_success_url(self):
        return reverse_lazy("event:viewallevent")
    

    def form_valid(self, form):
        event = form.save(commit=False)
        event.organized_by = self.request.user
        event.save()
        return super().form_valid(form)

# view for updaing Event
class UpdateEvent(PermissionRequiredMixin, UpdateView):
    permission_required = 'notice.can_view_add_remove_event'
    model = Event
    form_class = EventForm
    template_name = 'event/updateevent.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy("event:viewallevent")

# view to delete event  
class DeleteEvent(PermissionRequiredMixin, DeleteView):
    permission_required = 'notice.can_view_add_remove_event'
    model = Event
    template_name = 'event/deleteevent.html'
    def get_success_url(self):
        return reverse_lazy("event:viewallevent")
    