from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bios = models.TextField(blank=True, default='Create A Bios!')
    image = models.ImageField(
        upload_to='images/',
        default='https://res.cloudinary.com/drdelhvyt/image/upload/v1714060667/default_profile_qsg0aq.jpg', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    @property
    def public_tasks_count(self):
        return self.owner.owned_tasks.filter(task_visability=True).count()

    @property
    def joined_tasks_count(self):
        return self.owner.assigned_tasks.filter(task_visability=True).count()


def __str__(self):
    return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
