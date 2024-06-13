from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    CATEGORY_CHOICES = [
        ('Work', 'Work'),
        ('Personal', 'Personal'),
        ('Study', 'Study'),
        ('Other', 'Other'),
    ]

    STATE_CHOICES = [
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    ]

    VISABILITY_CHOICES = [
                         ('Private', 'Private'),
                         ('Public', 'Public'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES,
                                default='Medium')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES,
                                default='Other')
    state = models.CharField(max_length=20, choices=STATE_CHOICES,
                             default='In Progress')
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='owned_tasks')
    assigned_users = models.ManyToManyField(User,
                                            related_name='assigned_tasks',
                                            blank=True)
    state_changed_by = models.ForeignKey(User, on_delete=models.SET_NULL,
                                         null=True, blank=True,
                                         related_name='state_changed_tasks')
    task_visability = models.CharField(max_length=20,
                                       choices=VISABILITY_CHOICES,
                                       default='Private')
    task_messages = models.ManyToManyField('task_message.TaskMessage',
                                           blank=True)
                                           