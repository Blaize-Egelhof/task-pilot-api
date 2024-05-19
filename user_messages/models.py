from django.db import models
from django.contrib.auth.models import User

# default=False for boolean fields

class Message(models.Model):
    related_task = models.ForeignKey('task.Task', on_delete=models.CASCADE)
    accepted = models.BooleanField(blank=True)  
    declined = models.BooleanField(blank=True)
    title = models.CharField(max_length=30)
    context= models.CharField(max_length=50)
    recipient_inbox = models.ForeignKey('inbox.Inbox', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    read_status = models.BooleanField(default=False , blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
