from django.db import models
from users.models import CustomUser, Student

# Create your models here.

class Event(models.Model):
    STATUS = (
        ('on-going', 'on-going'),
        ('completed', 'completed'),
    )
    name = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='on-going')
    organized_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class EventPrticipant(models.Model):
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event_id} {self.student_id}"