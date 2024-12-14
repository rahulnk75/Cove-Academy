from django.shortcuts import render,redirect
from Frontend . models import Contact_Db
from Backend . models import Exam_Db,Course_Db,Subject_Db

# Create your views here.
def Courses_Filterd(request,Cour_name):
    cour=Course_Db.objects.filter(Exam_Categories=Cour_name)
    return render(request,'course_filterd.html',{'cour':cour}) 

def Subject_Filterd(request,sub_name):
    sub=Subject_Db.objects.filter(Course_Name=sub_name)
    return render(request,'subject_filterd.html',{'sub':sub})

def Explore_Course(request,Ex_id):
    Ex_course=Course_Db.objects.filter(id=Ex_id)
    return render(request,'explore_course.html',{'Ex_course':Ex_course})

def All_Classes(request,):
    sub=Subject_Db.objects.all()
    return render(request,'all_classes.html',{sub:sub})
