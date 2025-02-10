from django.shortcuts import render,redirect
from Backend.models import Exam_Db,Course_Db,Subject_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from StudentsApp.models import Register_Db
from MentorsApp. models import Mentors_Register_Db,Record_Class_Db
from Frontend.models import Contact_Db
from django.contrib import messages
from CourseApp.models import Payment_DB,Subject_Payment_DB,Course_Comments_DB
from django.db.models import Sum, Count 

# start exam categotys

def index_page(request):
    C_comment_=Course_Comments_DB.objects.all()
    details=Record_Class_Db.objects.all()
    course_revenue = Payment_DB.objects.aggregate(total_revenue=Sum('Course_Fees'))
    course_student_count = Payment_DB.objects.aggregate (total_students=Count('id'))

    subject_revenue = Subject_Payment_DB.objects.aggregate(total_revenue=Sum('Subject_Fees'))
    subject_student_count = Subject_Payment_DB.objects.aggregate(total_students=Count('id'))

    total_revenue = (course_revenue['total_revenue'] or 0) + (subject_revenue['total_revenue'] or 0)
    total_students = (course_student_count['total_students'] or 0) + (subject_student_count['total_students'] or 0)
   
    return render(request, 'index.html', {
        'course_revenue': course_revenue['total_revenue'] or 0,
        'course_student_count': course_student_count['total_students'] or 0,
        'subject_revenue': subject_revenue['total_revenue'] or 0,
        'subject_student_count': subject_student_count['total_students'] or 0,
        'total_revenue': total_revenue,
        'total_students': total_students,
        'details':details,
        'C_comment_':C_comment_,
    })


def Exam_Category(request):
    obj=Exam_Db.objects.all()
    return render(request,'exam_category.html',{"obj":obj})

def Save_Exam_Category(request):
    if request.method =='POST':
        _Exam_Category=request.POST.get('Exam_Category_')
        _Description=request.POST.get('Description_')
        _Images=request.FILES['Images_']
        obj=Exam_Db(Exam_Category=_Exam_Category,Description=_Description,Images=_Images)
        obj.save()
        messages.success(request,"Item Added Successfully...!!!")
        return redirect(Exam_Category)
        
def Display_Exam_Category(request):
    display=Exam_Db.objects.all()
    return render(request,'display_exam_category.html',{'display':display})

def Delete_Exam_Category(request,del_id):
    remove=Exam_Db.objects.get(id=del_id)
    remove.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Display_Exam_Category)

def Edit_Exam_Category(request,edit_id):
    edit=Exam_Db.objects.get(id=edit_id)
    return render(request,'edit_exam_category.html',{'edit':edit})

def Upload_Exam_Category(request,upd_id):
     if request.method =='POST':
        _Exam_Category=request.POST.get('Exam_Category_')
        _Description=request.POST.get('Description_')
        try:
            _Images=request.FILES['Images_']
            fs=FileSystemStorage()
            image=fs.save(_Images.name,_Images)
        except MultiValueDictKeyError:
            image=Exam_Db.objects.get(id=upd_id).Images

        Exam_Db.objects.filter(id=upd_id).update(Exam_Category=_Exam_Category,Description=_Description,Images=image)
        messages.success(request,"Successfully Updated...!!!")
        return redirect(Display_Exam_Category)
# end exam categotys
# start course details
def Add_Course(request):
    cat=Exam_Db.objects.all()
    return render(request,'add_course.html',{'cat':cat})


def Save_Course(request):
     if request.method =='POST':
          _Exam_Categories=request.POST.get('Exam_Categories_')
          _Exam_Name=request.POST.get('Exam_Name_')
          _Course_Name=request.POST.get('Course_Name_')
          _Course_fees=request.POST.get('Course_fees_')
          _old_fees=request.POST.get('old_fees_')
          _Course_Images=request.FILES['Course_Images_']
          _Description=request.POST.get('Description_')
          obj=Course_Db(Exam_Categories=_Exam_Categories,Exam_Name=_Exam_Name,
                        Course_Name=_Course_Name,Course_fees=_Course_fees,Course_Images=_Course_Images,
                        Description=_Description,Old_fees=_old_fees)
          obj.save()
          messages.success(request,"Item Added Successfully...!!!")
          return redirect(Add_Course)
     
def Dispaly_Course(request):
    dis=Course_Db.objects.all()
    return render(request,'display_course.html',{'dis':dis})

def Delete_Course(request,del_id):
    delt=Course_Db.objects.filter(id=del_id)
    delt.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Dispaly_Course)

def Edit_Course(request,edit_id):
    cat=Exam_Db.objects.all()
    edit=Course_Db.objects.get(id=edit_id)
    return render(request,'edit_course.html',{'edit':edit,'cat':cat})

def Upload_Course(request,upd_id):
     if request.method =='POST':
          _Exam_Categories=request.POST.get('Exam_Categories_')
          _Exam_Name=request.POST.get('Exam_Name_')
          _Course_Name=request.POST.get('Course_Name_')
          _Course_fees=request.POST.get('Course_fees_')
          _old_fees=request.POST.get('old_fees_')
          try:
              _Course_Images=request.FILES['Course_Images_']
              fs=FileSystemStorage()
              _image=fs.save(_Course_Images.name,_Course_Images)
          except MultiValueDictKeyError:
              _image=Course_Db.objects.get(id=upd_id).Course_Images

        
          _Description=request.POST.get('Description_')
          Course_Db.objects.filter(id=upd_id).update(Exam_Categories=_Exam_Categories,Exam_Name=_Exam_Name,
                        Course_Name=_Course_Name,Course_fees=_Course_fees,Course_Images=_image,Description=_Description,Old_fees=_old_fees)
          messages.success(request,"Successfully Updated...!!!")
          return redirect(Dispaly_Course)
     
# end course details
# start subject details


def Add_Subject(request):
    exam=Exam_Db.objects.all()
    course=Course_Db.objects.all()
    return render(request,'add_subject.html',{'exam':exam,'course':course})

def Save_Subject(request):
     if request.method =='POST':
          _Course_name=request.POST.get('Course_name_')
          _Subject_Name=request.POST.get('Subject_Name_')
          _Description=request.POST.get('Description_')
          _Subject_Images=request.FILES['Subject_Images_']
          _Subject_fees=request.POST.get('Subject_fees_')
          _old_fees=request.POST.get('old_fees_')
          obj=Subject_Db(Course_Name=_Course_name,Subject_Name=_Subject_Name,Description=_Description,Subject_Images=_Subject_Images,
                         Subject_fees=_Subject_fees,Old_fees=_old_fees)
          obj.save()
          messages.success(request,"Item Added Successfully...!!!")
          return redirect(Add_Subject)

def Display_Subject(request):
    sub=Subject_Db.objects.all()
    return render(request,'display_subject.html',{'sub':sub})

def Delete_Subject(request,sub_id):
    remov=Subject_Db.objects.filter(id=sub_id)
    remov.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Display_Subject)


def Edit_Subject(request,edit_id):
    course=Course_Db.objects.all()
    edit=Subject_Db.objects.get(id=edit_id)
    return render(request,'edit_subject.html',{'edit':edit,'course':course})
          
def Update_Subject(request,upd_id):
     if request.method =='POST':
          _Course_name=request.POST.get('Course_name_')
          _Subject_Name=request.POST.get('Subject_Name_')
          _Subject_fees=request.POST.get('Subject_fees_')
          _old_fees=request.POST.get('old_fees_')
         
          try:
              _Subject_Images=request.FILES['Subject_Images_']
              fs=FileSystemStorage()
              _image=fs.save(_Subject_Images.name,_Subject_Images)

          except MultiValueDictKeyError:
              _image=Subject_Db.objects.get(id=upd_id).Subject_Images


          _Description=request.POST.get('Description_')
          Subject_Db.objects.filter(id=upd_id).update(Course_Name=_Course_name,Subject_Name=_Subject_Name,Description=_Description,
                                                      Subject_Images=_image,Subject_fees=_Subject_fees,Old_fees=_old_fees)
          messages.success(request,"Successfully Updated...!!!")
          return redirect(Display_Subject)

# end subject details         
# start admin login 
def Login_Page(request):
    return render(request,'login_page.html')

def Admin_Login(request):
    if request.method =='POST':
        _user_name=request.POST.get('user_name_')
        _password=request.POST.get('password_')
        if User.objects.filter(username__contains=_user_name).exists():
            _user=authenticate(username=_user_name,password=_password)
            if _user is not None:
                login(request,_user)
                request.session['username']=_user_name
                request.session['password']=_password
                messages.success(request,"Welcome to Cove Academy")
                return redirect(index_page)
            else:
                messages.error(request,'Invalid Username...!!!')
                return redirect(Login_Page)
        else:
            messages.error(request,'Invalid Password...!!!')
            return redirect(Login_Page)     
        
def Admin_Logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"Logout successfully...!!!") 
    return redirect(Login_Page) 
# end admin login

def Contact_display(request):
    dis=Contact_Db.objects.all()
    return render(request,'contact_display.html',{'dis':dis})

def Contact_delete(request,del_id):
    remov=Contact_Db.objects.filter(id=del_id)
    remov.delete()
    return redirect(Contact_display)

def Display_Register_Students(request):
    Reg=Register_Db.objects.all()
    return render(request,'display_register_students.html',{'Reg':Reg})

def Delete_Register_Students(request,del_id):
    remov=Register_Db.objects.filter(id=del_id)
    remov.delete()
    return redirect(Display_Register_Students)

def Display_Register_Mentors(request):
    Reg=Mentors_Register_Db.objects.all()
    return render(request,'display_register_mentors.html',{'Reg':Reg})

def Approve_Mentor(request, mentor_id):
    mentor = Mentors_Register_Db.objects.get(id=mentor_id)
    mentor.is_approved = True
    mentor.save()
    messages.success(request,"Approved Successfully...!!!")
    return redirect('Display_Register_Mentors')


def Delete_Register_Mentors(request,del_id):
    remov=Mentors_Register_Db.objects.filter(id=del_id)
    remov.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Display_Register_Mentors) 

def Display_Bought_Couserses(request):
    Course=Payment_DB.objects.all()
    return render(request,'display_bought_couserses.html',{'Course':Course})

def Remove_Display_Bought_Couserses(request,rem_id):
    remov=Payment_DB.objects.filter(id=rem_id)
    remov.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Display_Bought_Couserses)
    
def Display_Bought_Subjects(request):
    Subject=Subject_Payment_DB.objects.all()
    return render(request,'display_bought_subjects.html',{'Subject':Subject})  

def Remove_Display_Bought_Subjects(request,rem_id):
    remov=Subject_Payment_DB.objects.filter(id=rem_id)
    remov.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Display_Bought_Subjects)

# Start Comments Details
def Display_Course_Comment(request):
    comment=Course_Comments_DB.objects.all()
    return render(request,'display_course_comment.html',{'comment':comment})

def Delete_Course_Comments(request,del_id):
    remove=Course_Comments_DB.objects.filter(id=del_id)
    remove.delete()
    messages.success(request,"Item Deleted Successfully...!!!")
    return redirect(Display_Course_Comment)
# End Comments Details

