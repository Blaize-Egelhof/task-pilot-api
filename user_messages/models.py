from django.db import models
from django.contrib.auth.models import User

# default=False for boolean fields

class Message(models.Model):
    related_task = models.OneToOneField('task.Task', on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=True)  
    declined = models.BooleanField(blank=True)
    title = models.CharField(max_length=20)
    context= models.CharField(max_length=40)
    recipient_inbox = models.OneToOneField('inbox.Inbox', on_delete=models.CASCADE)
    sender = models.OneToOneField(User, on_delete=models.CASCADE)
    read_status = models.BooleanField(default=False , blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
