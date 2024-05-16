from django.db import models
from django.contrib.auth.models import User
from task.models import Task
from messages.models import Messages

class inbox(models.Model):
    id_of_user = models.OneToOneField(User, on_delete=models.CASCADE)
    messages = models.ManyToManyField(Messages)
    last_updated =models.DateTimeField(auto_now_add=True)

    @property
    def public_sent_messages_count(self):
        return self.messages.filter(sender=self.id_of_user).count()

    def public_recieved_messages_count(self):
        return self.messages.filter(recipient_inbox=self.id_of_user).count()

    def total_messages(self):
        return self.public_sent_messages_count + self.public_recieved_messages_count()
