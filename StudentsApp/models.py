from django.db import models
from django.utils.timezone import now
# Create your models here.
class Register_Db(models.Model): 
    Full_Name=models.CharField(max_length=200,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    User_Email=models.EmailField(max_length=200,null=True,blank=True)
    Password=models.IntegerField(null=True,blank=True)
    Confirm_Password=models.IntegerField(null=True,blank=True)
    OTP = models.CharField(max_length=6, null=True, blank=True)

    def __str__(self):
        return self.Full_Name

class ChatGroup(models.Model):
    course_name = models.CharField(max_length=200, unique=True)
    members = models.ManyToManyField(Register_Db, related_name='chat_groups')

    def __str__(self):
        return self.course_name

class Message(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE, related_name='messages')
    sender = models.CharField(max_length=200)  # Can store student name or email
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"{self.sender}: {self.content[:20]}..."


