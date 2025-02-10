from django.db import models


# Create your models here.
class Contact_Db(models.Model):
    Full_name=models.CharField(max_length=200,null=True,blank=True)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Course=models.CharField(max_length=200,null=True,blank=True)
    Message=models.TextField(max_length=200,null=True,blank=True)






