from django.db import models
from django.contrib.auth.models import User
from task.models import Task
from user_messages.models import Message
from django.db.models.signals import post_save
from django.dispatch import receiver

class Inbox(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='inbox')
    messages = models.ManyToManyField(Message, blank=True)
    last_updated =models.DateTimeField(auto_now=True)

    @property
    def public_sent_messages_count(self):
        return self.messages.filter(sender=self.id_of_user).count()

    def public_recieved_messages_count(self):
        return self.messages.filter(recipient_inbox=self.id_of_user).count()

    def total_messages(self):
        return self.public_sent_messages_count + self.public_recieved_messages_count()

@receiver(post_save, sender=User)

def create_inbox(sender, instance, created, **kwargs):
    if created:
        Inbox.objects.create(user=instance)

post_save.connect(create_inbox, sender=User)
