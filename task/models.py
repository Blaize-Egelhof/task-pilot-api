from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    """
      A model representing a task with various attributes.
      Attributes:
      - title (CharField): The title of the task.
      - description (TextField): Detailed description of the task.
      - due_date (DateField): Deadline for completing the task.
      - priority (CharField): Priority level of the task
        (choices: 'High', 'Medium', 'Low').
      - category (CharField): Category of the task
        (choices: 'Work', 'Personal', 'Study', 'Other').
      - state (CharField): Current state of the task
        (choices: 'In Progress', 'Done').
      - created_at (DateTimeField): Date and time when the task was created.
      - owner (ForeignKey to User): The user who owns this task.
      - assigned_users (ManyToManyField to User):
        Users assigned to work on this task.
      - state_changed_by (ForeignKey to User):
        User who last changed the state of the task.
      - task_visibility (CharField): Visibility setting of the task
        (choices: 'Private', 'Public').
      - task_messages (ManyToManyField to 'task_message.TaskMessage'):
        Messages related to this task.
      Note:
      - Tasks can have multiple assigned users and messages.
      - Visibility determines whether a task is visible to all users or
        restricted to its owner and assigned users.
      """
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
