from django.db import models
from users.models import CustomUser
# Create your models here.

class Notice(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject
    
