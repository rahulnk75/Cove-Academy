from django.db import models
from datetime import date


# Create your models here.

class Payment_DB(models.Model):
    Full_Name = models.CharField(max_length=200, null=True, blank=True)
    Email = models.EmailField(max_length=200, null=True, blank=True)
    Course_Name = models.CharField(max_length=200, null=True, blank=True)
    Course_Fees = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.Full_Name} - {self.Course_Name}"


class Subject_Payment_DB(models.Model):
    Full_Name=models.CharField(max_length=200,null=True,blank=True)
    Subject_Email=models.EmailField(max_length=200,null=True,blank=True)
    Subject_Name=models.CharField(max_length=200,null=True,blank=True)
    Subject_Fees=models.IntegerField(null=True,blank=True)
    
class Course_Comments_DB(models.Model):
    C_User=models.CharField(max_length=200,null=True,blank=True)
    C_Cours_Name=models.EmailField(max_length=200,null=True,blank=True)
    C_Comment=models.CharField(max_length=200,null=True,blank=True)
    C_Date = models.DateField(default=date.today)
    C_Time = models.TimeField(auto_now_add=True,null=True, blank=True)    

