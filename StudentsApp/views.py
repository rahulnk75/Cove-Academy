from django.shortcuts import render,redirect
from StudentsApp . models import Register_Db
from Frontend .views import Home_Page

# Create your views here.
def Student_Register(request):
    return render(request,'student_register.html')

def Save_Student_Register(request):
    if request.method=='POST':
        _username=request.POST.get('username_')
        _p_number=request.POST.get('p_number_')
        _email=request.POST.get('email_')
        _password=request.POST.get('password_')
        _c_password=request.POST.get('c_password_')
        obj=Register_Db(Username=_username,Mobile=_p_number,Email=_email,Password=_password,C_Password=_c_password)
        obj.save()
        return redirect(Student_Register)
def Student_LogIn(request):
    return render(request,'student_login.html')

def Save_Student_LogIn(request):
     if request.method=='POST':
        _Username=request.POST.get('Username_')
        _Password=request.POST.get('Password_')
        if Register_Db.objects.filter(Username=_Username,Password=_Password).exists():
            request.session['Username']=_Username
            request.session['Password']=_Password
            return redirect(Home_Page)
        else:
            return redirect(Student_LogIn)
     else:
          return redirect(Student_LogIn)

def Student_Logout(request):
    del request.session['Username']
    del request.session['Password']
    return redirect(Home_Page)