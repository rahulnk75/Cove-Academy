from django.db import models

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
    is_approved = models.BooleanField(default=False)
     
    def __str__(self):
        return self.Full_Name






