from django.shortcuts import render,redirect
from django.http import HttpResponse
from MentorsApp.models import TextBook_Db,Study_Material_Db,Question_Paper_Db,Mentors_Register_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


# Create your views here.
def Mentors_Home_Page(request):
    return render(request,'mentors_home_page.html')

# start Mentors details 

def Mentors_Register(request):
    return render(request,'mentors_register.html')

def Save_Mentors_Register(request):
    if request.method =='POST':
        _full_name=request.POST.get('full_name_')
        _mobile=request.POST.get('mobile_')
        _email=request.POST.get('email_')
        _qualification=request.POST.get('qualification_')
        _experience=request.POST.get('experience_')
        _password=request.POST.get('password_')
        _c_password=request.POST.get('c_password_')
        obj=Mentors_Register_Db(Full_Name=_full_name,Mobile=_mobile,Email=_email,Qualification=_qualification,
                                Experience=_experience,Password=_password,C_password=_c_password)
        obj.save()
        messages.success(request, 'Account created successfully. Please wait for admin approval.')
        return redirect(Mentors_Login)
    else:
        messages.error(request, 'Password and confirm password do not match.')


def Mentors_Login(request):
    Mentors=Mentors_Register_Db.objects.order_by('-id').first()
    return render(request,'mentors_login.html',{'Mentors':Mentors})

def Save_Mentors_Login(request):
    if request.method =='POST':
        _email=request.POST.get('email_')
        _password=request.POST.get('password_')
        try:
            mentor = Mentors_Register_Db.objects.get(Email=_email)
            if mentor.Password==_password:
                if mentor.is_approved:
                   request.session['Email']=_email
                   request.session['Password']=_password  
                   messages.success(request,"Welcome to Cove Academy")
                   return redirect(Mentors_Home_Page)
                else:
                    messages.error(request, 'You are not approved yet Please wait...!!!')
            else:
                messages.error(request, 'Invalid password...!!!')
        except Mentors_Register_Db.DoesNotExist:
            messages.error(request, 'Invalid email...!!!')
    return redirect(Mentors_Login)

def Mentors_Logout(request):
    del request.session['Email']
    messages.success(request,"Logout successfully...!!!") 
    return redirect(Mentors_Login)
 
# End Mentors details
# start Text Book Details

def Add_Textbook_Page(request): 
    return render(request,'add_textbook_page.html')

def Save_Textbook(request):
    if request.method =='POST':
        _Subject_Name=request.POST.get('Subject_Name_')
        _Scert_Ncert=request.POST.get('Scert_Ncert_')
        _Class=request.POST.get('Class_')
        _PDF_file=request.FILES['PDF_file_']
        _Textbook_Images=request.FILES['Textbook_Images_']
        _Description=request.POST.get('Description_')
        obj=TextBook_Db(Subject_name=_Subject_Name,Scert_Ncert=_Scert_Ncert,Class=_Class,PDF_file=_PDF_file,Textbook_Images=_Textbook_Images,Description=_Description)
        obj.save()
        return redirect(Add_Textbook_Page)

def Download_PDF_Textbook(request, pk):
    if request.method == 'GET':
        textbook = TextBook_Db.objects.get(pk=pk)
        pdf_file = textbook.PDF_file
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % pdf_file.name
        return response

def Display_Textbook(request):
    view=TextBook_Db.objects.all()
    return render(request,'display_textbook.html',{'view':view})

def Delete_Textbook(request,del_id):
    delt=TextBook_Db.objects.filter(id=del_id)
    delt.delete()
    return redirect(Display_Textbook)

def Edit_Textbook(request,edit_id):
    edit=TextBook_Db.objects.get(id=edit_id)
    return render(request,'edit_textbook.html',{'edit':edit})

def Upload_Textbook(request,upd_id):
    if request.method =='POST':
        _Subject_Name=request.POST.get('Subject_Name_')
        _Scert_Ncert=request.POST.get('Scert_Ncert_')
        _Class=request.POST.get('Class_')
        try:
            _PDF_file=request.FILES['PDF_file_']
            P_fs=FileSystemStorage()
            Pdf_file=P_fs.save(_PDF_file.name,_PDF_file)
        except MultiValueDictKeyError:
            Pdf_file=TextBook_Db.objects.get(id=upd_id).PDF_file
        try:
            _Textbook_Images=request.FILES['Textbook_Images_']
            fs=FileSystemStorage()
            t_image=fs.save(_Textbook_Images.name,_Textbook_Images)
        except MultiValueDictKeyError:
            t_image=TextBook_Db.objects.get(id=upd_id).Textbook_Images

        _Description=request.POST.get('Description_')
        TextBook_Db.objects.filter(id=upd_id).update(Subject_name=_Subject_Name,Scert_Ncert=_Scert_Ncert,Class=_Class,PDF_file=Pdf_file,Textbook_Images=t_image,Description=_Description)
        return redirect(Display_Textbook)

# End TextBook Details
# start Study material Details

def Add_Study_Material(request): 
    return render(request,'add_study_material.html')

def Save_Study_Material(request):
    if request.method =='POST':
        _Subject_Name=request.POST.get('Subject_Name_')
        _Topic=request.POST.get('Topic_')
        _S_Pdf_file_=request.FILES['S_Pdf_file_']
        _Description=request.POST.get('Description_')
        obj=Study_Material_Db(Subject_name=_Subject_Name,Topic=_Topic,S_PDF_file=_S_Pdf_file_,Description=_Description)
        obj.save()
        return redirect(Add_Study_Material)

def Download_PDF_Study_Material(request, pk):
    if request.method == 'GET':
        textbook = Study_Material_Db.objects.get(pk=pk)
        pdf_file = textbook.S_PDF_file
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % pdf_file.name
        return response

def Display_Study_Material(request):
    view=Study_Material_Db.objects.all()
    return render(request,'display_study_material.html',{'view':view})

def Delete_Study_Material(request,del_id):
    delt=Study_Material_Db.objects.filter(id=del_id)
    delt.delete()
    return redirect(Display_Study_Material)

def Edit_Study_Material(request,edit_id):
    edit=Study_Material_Db.objects.get(id=edit_id)
    return render(request,'edit_study_saterial.html',{'edit':edit})

def Upload_Study_Material(request,upd_id):
    if request.method =='POST':
        _Subject_Name=request.POST.get('Subject_Name_')
        _Topic=request.POST.get('Topic_')
        try:
            _S_Pdf_file_=request.FILES['S_Pdf_file_']
            P_fs=FileSystemStorage()
            S_Pdf_file=P_fs.save(_S_Pdf_file_.name,_S_Pdf_file_)
        except MultiValueDictKeyError:
            S_Pdf_file=Study_Material_Db.objects.get(id=upd_id).S_PDF_file

        _Description=request.POST.get('Description_')
        Study_Material_Db.objects.filter(id=upd_id).update(Subject_name=_Subject_Name,Topic=_Topic,S_PDF_file=S_Pdf_file,Description=_Description)
        return redirect(Display_Study_Material)
# End Study material Details
# start Question Paper Details
def Add_Question_Paper(request): 
    return render(request,'add_question_paper.html')

def Save_Question_Paper(request):
    if request.method =='POST':
        _Exam_Name=request.POST.get('Exam_Name_')
        _Date=request.POST.get('Date_')
        _Q_Pdf_file_=request.FILES['Q_Pdf_file_']
        _Description=request.POST.get('Description_')
        obj=Question_Paper_Db(Exam_Name=_Exam_Name,Date=_Date,Q_PDF_file=_Q_Pdf_file_,Description=_Description)
        obj.save()
        return redirect(Add_Study_Material)

def Download_PDF_Question_Paper(request, pk):
    if request.method == 'GET':
        textbook = Question_Paper_Db.objects.get(pk=pk)
        pdf_file = textbook.Q_PDF_file
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % pdf_file.name
        return response

def Display_Question_Paper(request):
    view=Question_Paper_Db.objects.all()
    return render(request,'display_question_paper.html',{'view':view})

def Delete_Question_Paper(request,del_id):
    delt=Question_Paper_Db.objects.filter(id=del_id)
    delt.delete()
    return redirect(Display_Question_Paper)

def Edit_Question_Paper(request,edit_id):
    edit=Question_Paper_Db.objects.get(id=edit_id)
    return render(request,'edit_question_paper.html',{'edit':edit})

def Upload_Question_Paper(request,upd_id):
    if request.method =='POST':
        _Exam_Name=request.POST.get('Exam_Name_')
        _Date=request.POST.get('Date_')
        try:
            _Q_Pdf_file_=request.FILES['Q_Pdf_file_']
            P_fs=FileSystemStorage()
            Q_Pdf_file=P_fs.save(_Q_Pdf_file_.name,_Q_Pdf_file_)
        except MultiValueDictKeyError:
            Q_Pdf_file=Question_Paper_Db.objects.get(id=upd_id).Q_PDF_file

        _Description=request.POST.get('Description_')
        Question_Paper_Db.objects.filter(id=upd_id).update(Exam_Name=_Exam_Name,Date=_Date,Q_PDF_file=Q_Pdf_file,Description=_Description)
        return redirect(Display_Question_Paper)

# End Question Paper Details

