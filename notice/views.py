from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Notice
from .forms import NoticeForm
# Create your views here.

# view for listing all the notice
class AllNotice(ListView):
    model = Notice
    context_object_name = 'notices'
    template_name = 'notice/notice.html'


# view to add notice
class AddNotice(PermissionRequiredMixin, CreateView):
    permission_required = 'notice.can_view_add_remove_notice'
    model = Notice    
    form_class = NoticeForm
    template_name = 'notice/addNotice.html'

    def get_success_url(self):
        return reverse_lazy("notice:viewallnotice")
    
    def form_valid(self, form):
        notice = form.save(commit=False)
        notice.user = self.request.user
        notice.save()
        return super().form_valid(form)


# view to update notice
class UpdateNotice(PermissionRequiredMixin, UpdateView):
    permission_required = 'notice.can_view_add_remove_notice'
    model = Notice
    form_class = NoticeForm
    template_name = 'notice/updatenotice.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse_lazy("notice:viewallnotice")


# view to delete the notice   
class DeleteNotice(PermissionRequiredMixin, DeleteView):
    permission_required = 'notice.can_view_add_remove_notice'
    model = Notice
    template_name = 'notice/deletenotice.html'
    def get_success_url(self):
        return reverse_lazy("notice:viewallnotice")
    