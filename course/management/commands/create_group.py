from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from notice.models import Notice
from event.models import Event
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # Create groups
        teacher, _ = Group.objects.get_or_create(name='teacher')
        student, _ = Group.objects.get_or_create(name='student')
        Principal, _ = Group.objects.get_or_create(name='Principal')


        # Code to add permission to group ???
        ct_notice = ContentType.objects.get_for_model(Notice)
        ct_event = ContentType.objects.get_for_model(Event)


        # Now what - Say I want to add 'Can add project' permission to new_group?
        permission1 = Permission.objects.create(codename='can_view_add_remove_notices',
                                        name='Can add view remove notice',
                                        content_type=ct_notice)
        
        permission2 = Permission.objects.create(codename='can_view_add_remove_events',
                                        name='Can add view remove event',
                                        content_type=ct_event)
        
        teacher.permissions.add(permission1, permission2)
