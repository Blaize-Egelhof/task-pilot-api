from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Q


class Profile(models.Model):

    """
    A model representing a user profile linked to a User instance.
    Each user has a single Profile instance associated with their account,
    allowing customization of profile details such as biography and image.
    This model is auto created upon a new User instance being created
    """

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bios = models.TextField(blank=True, default='Create A Bios!')
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_qsg0aq', blank=True
    )

    class Meta:
        """
        Meta class for ordering all profiles from newest to oldest
        """
        ordering = ['-created_at']


def create_profile(sender, instance, created, **kwargs):

    """
    Signal receiver function to create a Profile,
    instance whenever a new User instance is created.
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
