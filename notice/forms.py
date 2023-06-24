from typing import Any
from django import forms
from .models import Notice

class NoticeForm(forms.ModelForm):

    class Meta:
        model = Notice
        fields = ['subject', 'body']

    # apply same css class to all the field in the form
    def __init__(self, *args, **kwargs):
        super(NoticeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
