from django.shortcuts import render,redirect
from Frontend . models import Contact_Db
from MentorsApp. models import TextBook_Db,Study_Material_Db,Question_Paper_Db,Record_Class_Db
from Backend . models import Exam_Db,Course_Db,Subject_Db

# Create your views here. 
def Home_Page(request):
    exam=Exam_Db.objects.all()
    Course=Course_Db.objects.all()
    subject=Subject_Db.objects.all() 
    Text=TextBook_Db.objects.all()
    return render(request,'home_page.html',{'exam':exam,'Course':Course,'subject':subject,'Text':Text})

def About_Page(request):
    return render(request,'about_page.html')

def Contact_Page(request):
    return render(request,'Contact_page.html')

def Save_Contact(request):
    if request.method=='POST':
        _Full_Name=request.POST.get('Full_Name_')
        _Email=request.POST.get('Email_')
        _Mobile=request.POST.get('Mobile_')
        _Course=request.POST.get('Course_')
        _Message=request.POST.get('Message_')
        obj=Contact_Db(Full_name=_Full_Name,Email=_Email,Mobile=_Mobile,Course=_Course,Message=_Message)
        obj.save()
        return redirect(Contact_Page)
 
def Course_Page(request):
    Course=Course_Db.objects.all()
    return render(request,'course_page.html',{'Course':Course}) 

def Subject_Page(request):
    Class=Record_Class_Db.objects.all()
    Subject=Subject_Db.objects.all()
    return render(request,'subject_page.html',{'Subject':Subject,'Class':Class})

def Blog_page(request):  
    return render(request,'blog_page.html')

def View_Textbook_Page(request): 
    view=TextBook_Db.objects.all()
    return render(request,'view_textbook_page.html',{'view':view})

def View_Study_Material(request):
    view=Study_Material_Db.objects.all()
    return render(request,'view_study_material.html',{'view':view})

def View_Question_Paper(request):
    view=Question_Paper_Db.objects.all()
    return render(request,'view_question_Paper.html',{'view':view})

def Edit_Profile(request):
    return render(request,'edit_profile.html')  

def Chat_Page(request):
    return render(request,'Chat_page.html')

def Live_Class_Page(request):
    return render(request,'live_class_page.html')

def Mock_Test_Page(request):
    return render(request,'mock_test_page.html')