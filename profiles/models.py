from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    bios = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../https://res.cloudinary.com/drdelhvyt/image/upload/v1715765148/taskpilot/ffomfbsj8j1wjaiqi5r5.jpg>', blank=True
    )
    # Automatically Query the Tasks Model as soon as this model is rendered , task needs to be owned by the user and status of task needs to be public

    class Meta:
        ordering = ['-created_at']

    @property
    def public_tasks_count(self):
        return self.owner.owned_tasks.filter(is_public=True).count()

    @property
    def joined_tasks_count(self):
        return self.owner.assigned_tasks.filter(is_public=True).count()

