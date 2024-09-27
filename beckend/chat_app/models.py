from django.db import models
# from django.contrib.auth.models import User
# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()  # Use this to avoid direct import


class UserMessage(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    time_stamp=models.DateTimeField(auto_now_add=True)
    message=models.TextField()



class AdminReply(models.Model):
    reply_message=models.ForeignKey(UserMessage,on_delete=models.CASCADE,default=1)
    admin=models.ForeignKey(User,on_delete=models.CASCADE)
    message=models.TextField(default="write reply here")
    time_stamp=models.DateTimeField(auto_now_add=True)
