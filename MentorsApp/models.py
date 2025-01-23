from django.db import models
from datetime import date

# Create your models here.
class TextBook_Db(models.Model):
    Subject_name=models.CharField(max_length=200,null=True,blank=True)
    Scert_Ncert=models.CharField(max_length=200,null=True,blank=True)
    Class=models.CharField(max_length=200,null=True,blank=True)
    PDF_file=models.FileField(upload_to='Textbook_Pdfs',null=True,blank=True)
    Textbook_Images=models.ImageField(upload_to='Textbook_Images',null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)

class Study_Material_Db(models.Model):
    Subject_name=models.CharField(max_length=200,null=True,blank=True)
    Topic=models.CharField(max_length=200,null=True,blank=True)
    S_PDF_file=models.FileField(upload_to='Study_material_Pdfs',null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)

class Question_Paper_Db(models.Model):
    Exam_Name=models.CharField(max_length=200,null=True,blank=True)
    Date=models.CharField(max_length=200,null=True,blank=True)
    Q_PDF_file=models.FileField(upload_to='Study_material_Pdfs',null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)

 
class Mentors_Register_Db(models.Model):
    Full_Name=models.CharField(max_length=200,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    Email=models.EmailField(max_length=200,null=True,blank=True)
    Qualification=models.CharField(max_length=200,null=True,blank=True)
    Experience=models.CharField(max_length=200,null=True,blank=True)
    Password=models.CharField(max_length=200,null=True,blank=True)
    C_password=models.CharField(max_length=200,null=True,blank=True)
    OTP = models.CharField(max_length=6, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    
     
    def __str__(self):
        return self.Full_Name

class Record_Class_Db(models.Model):
    Mentors_Id = models.CharField(max_length=200, null=True, blank=True)
    Exam = models.CharField(max_length=200, null=True, blank=True)
    Course = models.CharField(max_length=200, null=True, blank=True)
    Subject = models.CharField(max_length=200, null=True, blank=True)
    Topic_Name = models.CharField(max_length=200, null=True, blank=True)
    Upload_Class = models.FileField(upload_to='videos/', null=True, blank=True)    
    Upload_PDF = models.FileField(upload_to='Record_class_Pdfs', null=True, blank=True)
    Description = models.TextField(max_length=200, null=True, blank=True)
    Video_Duration = models.DurationField(null=True, blank=True)
    Date = models.DateField(default=date.today) 
    Login_Time = models.TimeField(auto_now_add=True,null=True, blank=True) 
    Logout_Time = models.TimeField(auto_now=True,null=True, blank=True) 

    def __str__(self):
        return f"{self.Topic_Name} - {self.Subject}"


