from django.shortcuts import render,redirect,get_object_or_404
from Frontend . models import Contact_Db
from Backend . models import Course_Db,Subject_Db
import razorpay

# Create your views here.
def Courses_Filterd(request,Cour_name):
    cour=Course_Db.objects.filter(Exam_Categories=Cour_name)
    return render(request,'course_filterd.html',{'cour':cour}) 

def Subject_Filterd(request,sub_name,Ex_id):
    sub=Subject_Db.objects.filter(Course_Name=sub_name)
    Ex_course=Course_Db.objects.filter(id=Ex_id)
    return render(request,'subject_filterd.html',{'sub':sub,'Ex_course':Ex_course})

def Class_Page(request): 
    return render(request,'class_page.html')

def Payment_Page(request,pay_id):
    pay_p=Course_Db.objects.filter(id=pay_id)
    price=0
    discount=0
    total=0
    for i in pay_p:
        discount = i.Old_fees - i.Course_fees
    customer=Course_Db.objects.order_by('-id').first()
    payy=customer.Course_fees
    amount=int(payy*100)
    payy_str=str(amount)
    if request.method=="POST":
        order_currency= 'INR'
        client=razorpay.Client(auth=('rzp_test_sXSjc7ZbwI7M3J','JfZlKEyC2d0YJZDzcHX4eMjP'))
        payment = client.order.create({'amount':amount,'order_currency':order_currency})
    return render(request,'payment_page.html',{'pay_p':pay_p,'discount':discount,'payy_str':payy_str})


def Subject_Payment_Page(request,pay_id):
    pay_p=Subject_Db.objects.filter(id=pay_id)
    price=0
    discount=0
    total=0
    for i in pay_p: 
        discount = i.Old_fees - i.Subject_fees
    customer=Subject_Db.objects.order_by('-id').first()
    payy=customer.Subject_fees
    amount=int(payy*100)
    payy_str=str(amount)
    if request.method=="POST":
        order_currency= 'INR'
        client=razorpay.Client(auth=('rzp_test_sXSjc7ZbwI7M3J','JfZlKEyC2d0YJZDzcHX4eMjP'))
        payment = client.order.create({'amount':amount,'order_currency':order_currency})
    return render(request,'subject_payment_page.html',{'pay_p':pay_p,'discount':discount,'payy_str':payy_str})