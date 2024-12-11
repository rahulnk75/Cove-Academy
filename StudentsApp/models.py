from django.db import models

# Create your models here.
class Register_Db(models.Model): 
    Username=models.CharField(max_length=200,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Password=models.CharField(max_length=200,null=True,blank=True)
    C_Password=models.CharField(max_length=200,null=True,blank=True)
