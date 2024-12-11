from django.shortcuts import render,redirect
from Frontend . models import Contact_Db
from Backend . models import Exam_Db,Course_Db,Subject_Db

# Create your views here.
def Home_Page(request):
    exam=Exam_Db.objects.all()
    Course=Course_Db.objects.all()
    subject=Subject_Db.objects.all()
    return render(request,'home_page.html',{'exam':exam,'Course':Course,'subject':subject})

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

def Courses_Filterd(request,Cour_name):
    cour=Course_Db.objects.filter(Exam_Categories=Cour_name)
    return render(request,'course_filterd.html',{'cour':cour})  

def Subject_Page(request):
    Subject=Subject_Db.objects.all()
    return render(request,'subject_page.html',{'Subject':Subject})

def Subject_Filterd(request,sub_name):
    sub=Subject_Db.objects.filter(Course_Name=sub_name)
    return render(request,'subject_filterd.html',{'sub':sub})

def All_login_page(request):
    return render(request,'all_login_page.html')

def Textbook_Page(request): 
    return render(request,'textbook_page.html')

def Blog_page(request): 
    return render(request,'blog_page.html')