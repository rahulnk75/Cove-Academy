from django.db import models

# Create your models here.
class Register_Db(models.Model): 
    Full_Name=models.CharField(max_length=200,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    User_Email=models.EmailField(max_length=200,null=True,blank=True)
    Password=models.IntegerField(null=True,blank=True)
    Confirm_Password=models.IntegerField(null=True,blank=True)
    OTP = models.CharField(max_length=6, null=True, blank=True)
    
