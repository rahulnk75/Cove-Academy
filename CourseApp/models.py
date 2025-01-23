from django.db import models

# Create your models here.
class Payment_DB(models.Model):
    Full_Name=models.CharField(max_length=200,null=True,blank=True)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Course_Name=models.CharField(max_length=200,null=True,blank=True)
    Course_Fees=models.IntegerField(null=True,blank=True)

class Subject_Payment_DB(models.Model):
    Full_Name=models.CharField(max_length=200,null=True,blank=True)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Subject_Name=models.CharField(max_length=200,null=True,blank=True)
    Subject_Fees=models.IntegerField(null=True,blank=True)
   
