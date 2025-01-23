from django.db import models
from MentorsApp.models import Mentors_Register_Db

# Create your models here.
class Exam_Db(models.Model):
    Exam_Category=models.CharField(max_length=200,null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)
    Images=models.ImageField(upload_to='Exam_Images',null=True,blank=True)
 
class Course_Db(models.Model):
    Exam_Categories=models.CharField(max_length=200,null=True,blank=True)
    Exam_Name=models.TextField(max_length=200,null=True,blank=True)
    Course_Name=models.CharField(max_length=200,null=True,blank=True)
    Course_fees=models.IntegerField(null=True,blank=True)
    Old_fees=models.IntegerField(null=True,blank=True)
    Course_Images=models.ImageField(upload_to='Course_Images',null=True,blank=True)
    Description=models.TextField(max_length=200,null=True,blank=True)
     
class Subject_Db(models.Model):
    Course_Name=models.CharField(max_length=200,null=True,blank=True)
    Subject_Name=models.CharField(max_length=200,null=True,blank=True) 
    Description=models.TextField(max_length=200,null=True,blank=True)
    Subject_fees=models.IntegerField(null=True,blank=True)
    Old_fees=models.IntegerField(null=True,blank=True) 
    Subject_Images=models.ImageField(upload_to="Subject_Images",null=True,blank=True)
 
class CourseSale(models.Model):
    course = models.ForeignKey(Course_Db, on_delete=models.CASCADE)
    date_of_sale = models.DateField()
    quantity_sold = models.IntegerField()
    
class SubjectSale(models.Model):
    subject = models.ForeignKey(Subject_Db, on_delete=models.CASCADE)
    date_of_sale = models.DateField()
    quantity_sold = models.IntegerField()
