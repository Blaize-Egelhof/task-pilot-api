from django.db import models
from django.contrib.auth.models import User
from task.models import Task

class TaskMessage(models.Model):
    sender=models.ForeignKey(User,on_delete=models.CASCADE)
    associated_task = models.ForeignKey(Task,on_delete=models.CASCADE)
    title = models.CharField(max_length=20 ,blank=True)
    context = models.CharField(max_length =40 ,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
