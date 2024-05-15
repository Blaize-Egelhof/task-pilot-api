from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bios = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../v1715765148/taskpilot/ffomfbsj8j1wjaiqi5r5.jpg>', blank=True
    )
    class Meta:
        ordering = ['-created_at']

# Automatically Query the Tasks Model as soon as this model is rendered by related name , task needs to be owned by the user and status of task needs to be public
    @property
    def public_tasks_count(self):
        return self.owner.owned_tasks.filter(is_public=True).count()

    @property
    def joined_tasks_count(self):
        return self.owner.assigned_tasks.filter(is_public=True).count()

def __str__(self):
    return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# Signaling that as soon as a User instances is created , create a profile instance
post_save.connect(create_profile, sender=User)

