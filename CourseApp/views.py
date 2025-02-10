from django.shortcuts import render,redirect,get_object_or_404
from Frontend . models import Contact_Db
from Backend . models import Course_Db,Subject_Db
from StudentsApp .models import Register_Db
import razorpay
from django.contrib import messages
from MentorsApp.models import Record_Class_Db
from CourseApp.models import Payment_DB,Subject_Payment_DB,Course_Comments_DB
from Frontend.views import Course_Page,Edit_Profile


# Create your views here.
def Courses_Filterd(request,Cour_name):
    cour=Course_Db.objects.filter(Exam_Categories=Cour_name)
    return render(request,'course_filterd.html',{'cour':cour})  

def Subject_Filterd(request,sub_name,Ex_id):
    Com_user = Register_Db.objects.filter(User_Email=request.session.get('User_Email'))
    sub=Subject_Db.objects.filter(Course_Name=sub_name)
    Ex_course=Course_Db.objects.filter(id=Ex_id)
    return render(request,'subject_filterd.html',{'sub':sub,'Ex_course':Ex_course,'Com_user':Com_user})


def Class_Page(request, sub_id,sub_name_id): 
    sub_name=Subject_Db.objects.filter(id=sub_name_id)
    subject = get_object_or_404(Subject_Db, id=sub_id)
    classes = Record_Class_Db.objects.filter(Subject=subject.Subject_Name)
    return render(request, 'class_page.html', {'subject': subject, 'classes': classes,'sub_name':sub_name})

def Payment_Page(request, pay_id):
    obj = Register_Db.objects.filter(User_Email=request.session.get('User_Email'))
    pay_p = Course_Db.objects.filter(id=pay_id)
    discount = 0
    for course in pay_p: 
        discount = course.Old_fees - course.Course_fees
    customer = pay_p.first()
    amount = int(customer.Course_fees * 100)  
    payy_str = str(amount) 
    payment = None
    if request.method == "POST":
        client = razorpay.Client(auth=('rzp_test_sXSjc7ZbwI7M3J', 'JfZlKEyC2d0YJZDzcHX4eMjP'))
        payment = client.order.create({'amount': amount, 'currency': 'INR'})
    return render(request, 'payment_page.html', {'pay_p': pay_p,'discount': discount,'payy_str': payy_str,'obj': obj,'payment': payment,})

def Save_Payment_Page(request):
    if request.method=='POST':
        _Full_name=request.POST.get('Full_name_')
        _Email=request.POST.get('Email_')
        _Course_name=request.POST.get('Course_name_')
        _Course_fees=request.POST.get('Course_fees_')
        obj=Payment_DB(Full_Name=_Full_name,Email=_Email,Course_Name=_Course_name,Course_Fees=_Course_fees)
        obj.save()
        return redirect(Edit_Profile)
       

def Subject_Payment_Page(request, pay_id):
    obj = Register_Db.objects.filter(User_Email=request.session.get('User_Email'))
    pay_p = Subject_Db.objects.filter(id=pay_id)
    discount = 0
    for i in pay_p:
        discount = i.Old_fees - i.Subject_fees
    customer = pay_p.first()
    amount = int(customer.Subject_fees * 100) 
    payy_str = str(amount)
    payment = None
    if request.method == "POST":
        client = razorpay.Client(auth=('rzp_test_sXSjc7ZbwI7M3J', 'JfZlKEyC2d0YJZDzcHX4eMjP'))
        payment = client.order.create({'amount': amount, 'currency': 'INR'})
    return render(request, 'subject_payment_page.html', {'pay_p': pay_p,'discount': discount,'payy_str': payy_str, 'obj': obj,'payment': payment, })



def Save_Subject_Payment_Page(request):
    if request.method == 'POST':
        _Full_name = request.POST.get('Full_name_')
        _Email = request.POST.get('Email_')
        _Subject_Name = request.POST.get('Subject_Name_')
        _Subject_fees = request.POST.get('Subject_fees_')
        obj = Subject_Payment_DB(Full_Name=_Full_name,Subject_Email=_Email,Subject_Name=_Subject_Name, Subject_Fees=_Subject_fees)
        obj.save()
        return redirect(Edit_Profile)
    
def Save_Course_Comments(request):
    if request.method == 'POST':
        C_user=request.POST.get('C_user')
        C_Cours_name=request.POST.get('C_Cours_name')
        C_comment=request.POST.get('C_comment')
        Comment=Course_Comments_DB(C_User=C_user,C_Cours_Name=C_Cours_name,C_Comment=C_comment)
        Comment.save()
        messages.success(request,'Thank You For Your Comment...!!!')
        return redirect(Course_Page)
    

