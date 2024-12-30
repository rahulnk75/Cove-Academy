from django.shortcuts import render,redirect
from StudentsApp . models import Register_Db
from Frontend .views import Home_Page
from django.contrib import messages

# Create your views here.
def Student_Register(request):
    return render(request,'student_register.html')

def Save_Student_Register(request):
      if request.method=='POST':
        _full_name=request.POST.get('full_name_')
        _mobile=request.POST.get('mobile_')
        _email=request.POST.get('email_')
        _password=request.POST.get('password_')
        _c_password=request.POST.get('c_password_')
        stud=Register_Db(Full_Name=_full_name,Mobile=_mobile,Email=_email,Password=_password,Confirm_Password=_c_password)
        stud.save()
        messages.success(request,"Register successfully...!!!")
        return redirect(Student_LogIn)

def Student_LogIn(request):
    Student=Register_Db.objects.order_by('-id').first()
    return render(request,'student_login.html',{'Student':Student})

def Save_Student_LogIn(request):
    if request.method=='POST':
        _Username=request.POST.get('full_name_')
        _Password=request.POST.get('Password_')
        if Register_Db.objects.filter(Full_Name=_Username,Password=_Password).exists():
            request.session['Full_Name']=_Username
            request.session['Password']=_Password
            messages.success(request,"Welcome To Cove Academy")
            return redirect(Home_Page)
        else:
            messages.info(request,"Invalid Username...!!!")
            return redirect(Student_LogIn)    
    else:
        messages.info(request,"Password incorect...!!!")
        return redirect(Student_LogIn)

def Student_Logout(request): 
    del request.session['Full_Name']
    del request.session['Password']
    messages.success(request,"Logout successfully...!!!")
    return redirect(Student_LogIn)

def OTP_page(request):
    return render(request,'otp_page.html')