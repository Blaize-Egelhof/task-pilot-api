from django.db import models
from task.models import Task
from inbox.models import inbox
from django.contrib.auth.models import User

# default=False for boolean fields

class Message(modles.Model):
    related_task = models.OneToOneField(Task,on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=True)  
    declined = models.BooleanField(blank=True)
    title = models.CharField(max_length=20)
    context= models.CharField(max_length=40)
    recipient_inbox = models.OneToOneField(Inbox)
    sender = models.OneToOneField(User)
    read_status = models.BooleanField(default=False , blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
