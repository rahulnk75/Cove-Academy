from django.shortcuts import render,redirect
from StudentsApp . models import Register_Db
from Frontend .views import Home_Page
from django.contrib import messages
import random
from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string


# Create your views here.
# Start Student Register 
def Student_Register(request):
    return render(request, 'student_register.html')

def Save_Student_Register(request):
    if request.method == 'POST':
        _full_name = request.POST.get('full_name')
        _mobile = request.POST.get('mobile')
        _email = request.POST.get('email')
        _password = request.POST.get('password')
        _c_password = request.POST.get('c_password')

        if _password != _c_password:
            messages.error(request, "Passwords do not match.")
            return redirect(Student_Register)

        otp = str(random.randint(100000, 999999))
        stud = Register_Db(Full_Name=_full_name, Mobile=_mobile,User_Email=_email,Password=_password,Confirm_Password=_c_password,OTP=otp)
        stud.save()
        try:
            send_mail(
                subject='Your OTP for Registration',
                message=f'Hello {_full_name}, {otp} is your One Time Password (OTP) for Register at Cove Academy. This OTP will only be valid for 10 minutes jOC8hZpWbfx.Thanks,Cove Academy.',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[_email],
                fail_silently=False,  
            )
            request.session['email'] = _email
            messages.success(request, "OTP sent to your email. Please verify.")
            return redirect(Verify_OTP)
        except Exception as e:
            print(f"Error sending email: {e}")
            messages.error(request, "There was an issue sending the OTP. Please try again.")
            return redirect(Student_Register)

def Verify_OTP(request):
    Email_= Register_Db.objects.order_by('-id').first()
    if request.method == 'POST':
        email = request.session.get('email')
        otp = request.POST.get('otp')

        try:
            student = Register_Db.objects.get(User_Email=email, OTP=otp)
            student.OTP = None 
            student.save() 

            messages.success(request, "Registration complete! You can now log in.")
            return redirect(Student_LogIn)
        except Register_Db.DoesNotExist:
            messages.error(request, "Invalid OTP. Please try again.")
            return redirect(Verify_OTP)

    return render(request, 'verify_otp.html',{'Email_':Email_})

# End Student Register 
# Start Student Login

def Student_LogIn(request):
    return render(request,'student_login.html') 

def Save_Student_LogIn(request): 
    if request.method=='POST':
        _Email=request.POST.get('Email_')
        _Password=request.POST.get('Password_')
        if Register_Db.objects.filter(User_Email=_Email,Password=_Password).exists():
            request.session['User_Email']=_Email
            request.session['Password']=_Password
            messages.success(request,"Welcome To Cove Academy") 
            return redirect(Home_Page)
        else:
            messages.info(request,"Invalid Username...!!! Please First Register Then Login.")
            return redirect(Student_LogIn)    
    else:
        messages.info(request,"Password incorect...!!!")
        return redirect(Student_LogIn)

def Student_Logout(request): 
    del request.session['User_Email']
    del request.session['Password']
   
    messages.success(request,"Logout successfully...!!!")
    return redirect(Student_LogIn)
 
def ForgotPassword(request):
    return render(request, 'forgot_password.html')

def SendOTP(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        try:
            user = Register_Db.objects.get(Full_Name=full_name, User_Email=email)
            otp = str(random.randint(100000, 999999)) 
            user.OTP = otp
            user.save()
            request.session['full_name'] = full_name

            send_mail(
                'Password Reset OTP',
                f'Hello {full_name}, {otp} is your One Time Password (OTP) for ForgotPassword at Cove Academy. This OTP will only be valid for 10 minutes jOC8hZpWbfx.Thanks,Cove Academy.',
                'noreply@coveacademy.com',
                [email],
                fail_silently=False,
            )
            return redirect('VerifyOTP')
        except Register_Db.DoesNotExist:
            messages.error(request, "User with this email does not exist.")
            return redirect('forgot_password')
    return render(request, 'forgot_password.html')


def VerifyOTP(request):
    E_mail= Register_Db.objects.order_by('-id').first()
    if request.method == 'POST':
        otp = request.POST.get('otp')
        full_name = request.session.get('full_name') 
        
        if not full_name:
            messages.error(request, "Session expired. Please try again.")
            return redirect('forgot_password')

        try:
            user = Register_Db.objects.get(Full_Name=full_name)
            if user.OTP == otp:
                return redirect('reset_password')
            else:
                messages.error(request, "Invalid OTP. Please try again.")
                return redirect('VerifyOTP')
        except Register_Db.DoesNotExist:
            messages.error(request, "No such user exists.")
            return redirect('forgot_password')

    return render(request, 'reset_verify_otp.html',{'E_mail':E_mail})

def ResetPassword(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            full_name = request.session.get('full_name')
            if not full_name:
                messages.error(request, "Session expired. Please try again.")
                return redirect('forgot_password')

            try:
                user = Register_Db.objects.get(Full_Name=full_name)
                user.Password = new_password
                user.OTP = ""  
                user.save()
                messages.success(request, "Password reset successfully.")
                return redirect('Student_LogIn')
            except Register_Db.DoesNotExist:
                messages.error(request, "No such user exists.")
                return redirect('forgot_password')
        else:
            messages.error(request, "Passwords do not match.")
            return redirect('reset_password')
    
    return render(request, 'reset_password.html')


# End Student Login