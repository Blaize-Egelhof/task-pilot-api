from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q

"""
    A model representing a user profile linked to a User instance.

    Each user has a single Profile instance associated with their account,
    allowing customization of profile details such as biography, image, and
    tracking of owned and joined tasks.
"""


class Profile(models.Model):

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bios = models.TextField(blank=True, default='Create A Bios!')
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_qsg0aq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    @property
    def owned_tasks_count(self):
        """
        Returns the count of tasks owned by the user with task,
        visibility set to 'Public'.
        """
        return self.owner.owned_tasks.filter(task_visability='Public').count()

    @property
    def joined_tasks_count(self):
        """
        Returns the count of tasks where the user is ,
        assigned and task visibility is 'Public'.
        """
    return self.owner.assigned_tasks.filter(
        task_visability='Public'
    ).count()

    """
    Signal receiver function to create a Profile,
    instance whenever a new User instance is created.
    """


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
