from django.db import models
from django.contrib.auth.models import User
from task.models import Task

"""
Represents a message associated with a specific task in the system.

Attributes:
- sender (ForeignKey): User who sent the message.
- associated_task (ForeignKey): Task to which the message is associated.
- title (CharField): Title of the message (optional).
- context (CharField): Content or context of the message (optional).
- timestamp (DateTimeField): Date and time when the message was created.

Note:
- Each message is linked to a specific sender,
  (User) and an associated task (Task).
"""


class TaskMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    associated_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True)
    context = models.CharField(max_length=200, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
