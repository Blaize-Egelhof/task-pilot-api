# views.py
from rest_framework import ApiView

class TaskMessage(Model.models):
    sender=models.ForeignKey(User,on_delete=Models.CASCADE)
    associated_task = models.ForeignKey(Task,on_delete=Models.CASCADE)
    title = models.CharField(max_length=20)
    context = models.CharField(max_length =40)
    timestamp = models.DateTimeField(auto_now_add=True)
