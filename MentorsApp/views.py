from django.shortcuts import render,redirect
from django.http import HttpResponse
from MentorsApp.models import TextBook_Db,Study_Material_Db,Question_Paper_Db,Mentors_Register_Db,Record_Class_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from Backend.models import Exam_Db,Course_Db,Subject_Db
from django.http import JsonResponse
from moviepy.video.io.VideoFileClip import VideoFileClip
from datetime import timedelta
import random
from django.core.mail import send_mail
from django.conf import settings
import string 
from CourseApp.models import Payment_DB,Subject_Payment_DB

 
# Create your views here.

def Mentors_Home_Page(request):
    details=Record_Class_Db.objects.all()
    course_count = Course_Db.objects.count()
    subject_count = Subject_Db.objects.count()
    total_count = course_count + subject_count
    total_students = Payment_DB.objects.values('Email').distinct().count() + Subject_Payment_DB.objects.values('Email').distinct().count()
    return render(request, 'mentors_home_page.html',{'total_students': total_students,'course_count': course_count,'subject_count': subject_count,'total_count': total_count,'details':details})
    

# start Mentors details 
def Mentors_Register(request):
    return render(request,'mentors_register.html')


def Save_Mentors_Register(request):
    if request.method == 'POST':
        _full_name = request.POST.get('full_name_')
        _mobile = request.POST.get('mobile_')
        _email = request.POST.get('email_')
        _qualification = request.POST.get('qualification_')
        _experience = request.POST.get('experience_')
        _password = request.POST.get('password_')
        _c_password = request.POST.get('c_password_')

        if _password != _c_password:
            messages.error(request, 'Password and confirm password do not match.')
            return redirect('mentors_register')
        otp = str(random.randint(100000, 999999))

        obj = Mentors_Register_Db(Full_Name=_full_name,Mobile=_mobile,Email=_email,Qualification=_qualification,Experience=_experience,Password=_password,C_password=_c_password,OTP=otp)
        obj.save()
        request.session['email'] = _email
        send_mail(
            'Your OTP for Verification',
            f'Hello {_full_name}, {otp} is your One Time Password (OTP) for Register for Mentors at Cove Academy. This OTP will only be valid for 10 minutes jOC8hZpWbfx.Thanks,Cove Academy.',
            settings.DEFAULT_FROM_EMAIL,
            [_email],
            fail_silently=False
        )
        messages.info(request, 'Please verify using the OTP sent to your email.')
        return redirect('Verify_OTP_')
    return render(request, 'mentors_register.html')

def Verify_OTP_(request):
    Email_M= Mentors_Register_Db.objects.order_by('-id').first()
    if request.method == 'POST':
        otp = request.POST.get('otp_') 
        email = request.session.get('email')

        if not email:
            messages.error(request, 'Session expired. Please register again.')
            return redirect('mentors_register')

        try:
            mentor = Mentors_Register_Db.objects.get(Email=email, OTP=otp)
            mentor.Is_Verified = True
            mentor.OTP = None  
            mentor.save()

            messages.success(request, 'Account verified successfully. Please wait for admin approval.')
            return redirect('Mentors_Login')
        except Mentors_Register_Db.DoesNotExist:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'verify_otp_.html',{'Email_M':Email_M})


def Mentors_Login(request):
    Mentors=Mentors_Register_Db.objects.order_by('-id').first()
    return render(request,'mentors_login.html',{'Mentors':Mentors})

def Save_Mentors_Login(request):
    if request.method =='POST':
        Mentor_email=request.POST.get('email_') 
        _password=request.POST.get('password_')
        try:
            mentor = Mentors_Register_Db.objects.get(Email=Mentor_email,Password=_password) 
            if mentor.Password==_password:
                if mentor.is_approved:
                   request.session['Email']=Mentor_email
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

def Mentors_ForgotPassword(request):
    return render(request, 'mentors_forgotpassword.html')

def Mentors_SendOTP(request):
    if request.method == 'POST':
        _name = request.POST.get('name')
        _email = request.POST.get('email')
        
        try:
            mentor = Mentors_Register_Db.objects.get(Email=_email, Full_Name=_name)
            otp = ''.join(random.choices(string.digits, k=6)) 
            mentor.OTP = otp
            mentor.save()

            send_mail(
                'Your OTP for Password Reset',
                f'Hello {_name}, {otp} is your One Time Password (OTP) for Password Reset at Cove Academy. This OTP will only be valid for 10 minutes jOC8hZpWbfx.Thanks,Cove Academy.',
                'from@example.com', 
                [_email],
                fail_silently=False,
            )
            
            messages.success(request, 'OTP sent to your email!')
            return redirect('mentors_verifyotp')
        except Mentors_Register_Db.DoesNotExist:
            messages.error(request, 'No mentor found with that name and email.')
    return redirect('mentors_forgotpassword')

def Mentors_VerifyOTP(request):
    if request.method == 'POST':
        _otp = request.POST.get('otp')
        try:
            mentor = Mentors_Register_Db.objects.get(OTP=_otp)
            request.session['mentor_id'] = mentor.id  
            return redirect('mentors_resetpassword')
        except Mentors_Register_Db.DoesNotExist:
            messages.error(request, 'Invalid OTP, please try again.')
    return render(request, 'mentors_verifyotp.html')

def Mentors_ResetPassword(request):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        if new_password == confirm_password:
            mentor = Mentors_Register_Db.objects.get(id=request.session.get('mentor_id'))
            mentor.Password = new_password
            mentor.C_password = new_password 
            mentor.OTP = '' 
            mentor.save()

            messages.success(request, 'Password has been reset successfully.')
            return redirect('Mentors_Login')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'mentors_resetpassword.html')

def Mentors_Edit_Profile(request):
    return render(request,'mentors_edit_profile.html')
 
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
# Start Upload Class Details
def Upload_Record_Class(request):  
    Email_= Mentors_Register_Db.objects.filter(Email=request.session.get('Email'))
    exam=Exam_Db.objects.all()
    course=Course_Db.objects.all()
    subject=Subject_Db.objects.all()
    return render(request,'upload_cecord_class.html',{'exam':exam,'course':course,'subject':subject,'Email_':Email_})

def get_courses_by_exam(request):
    exam_category = request.GET.get('exam_category', '')
    courses = Course_Db.objects.filter(Exam_Categories=exam_category).values('Course_Name')
    return JsonResponse(list(courses), safe=False)

def get_subjects_by_course(request):
    course_name = request.GET.get('course_name', '')
    subjects = Subject_Db.objects.filter(Course_Name=course_name).values('Subject_Name')
    return JsonResponse(list(subjects), safe=False)

def Save_upload_record_class(request): 
    if request.method == "POST":
        Mentors_Id = request.POST.get("Mentors_Id")
        exam = request.POST.get("exam")
        course = request.POST.get("course")
        subject = request.POST.get("subject")
        topic_name = request.POST.get("Subject_Name_")
        description = request.POST.get("Description_")
        video_file = request.FILES.get("video_file_") 
        pdf_file = request.FILES.get("S_Pdf_file_")
        
        video_duration = None
        if video_file:
            fs = FileSystemStorage()
            file_path = fs.save(video_file.name, video_file)
            video_path = fs.path(file_path)
            try:
                clip = VideoFileClip(video_path)
                video_duration_seconds = clip.duration  
                clip.close()
                video_duration = timedelta(seconds=video_duration_seconds)
            except Exception as e:
                print(f"Error calculating video duration: {e}")
            finally:
                fs.delete(file_path)
        record = Record_Class_Db(Mentors_Id=Mentors_Id,Exam=exam,Course=course,Subject=subject,Topic_Name=topic_name,Description=description,Upload_Class=video_file,Upload_PDF=pdf_file,Video_Duration=video_duration)
        record.save()
        return redirect("Upload_Record_Class")
    
def Display_Rcecord_Class(request):
    dis=Record_Class_Db.objects.all()
    return render(request,'display_rcecord_class.html',{'dis':dis})

def Download_PDF_Rcecord_Class(request, pk):
    if request.method == 'GET':
        textbook = Record_Class_Db.objects.get(pk=pk)
        pdf_file = textbook.Upload_PDF
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % pdf_file.name
        return response
    
def Delete_Rcecord_Class(request,del_id):
    delt=Record_Class_Db.objects.filter(id=del_id)
    delt.delete()
    return redirect(Display_Rcecord_Class)


def Edit_Rcecord_Class(request,edit_id):
    edit=Record_Class_Db.objects.get(id=edit_id)
    exam=Exam_Db.objects.all()
    course=Course_Db.objects.all()
    subject=Subject_Db.objects.all()
    return render(request,'edit_rcecord_class.html',{'edit':edit,'exam':exam,'course':course,'subject':subject})

def Upload_Upload_Record_Class(request, upd_id):
    if request.method == "POST":
        Mentors_Id = request.POST.get("Mentors_Id")
        exam = request.POST.get("exam")
        course = request.POST.get("course")
        subject = request.POST.get("subject")
        topic_name = request.POST.get("Subject_Name_")
        description = request.POST.get("Description_")
        video_file = request.FILES.get("video_file_")

        try:
            if video_file:
                fs = FileSystemStorage()
                video_path = fs.save(video_file.name, video_file)
                video_duration = None
                try:
                    clip = VideoFileClip(fs.path(video_path))
                    video_duration_seconds = clip.duration
                    clip.close()
                    video_duration = timedelta(seconds=video_duration_seconds)
                except Exception as e:
                    print(f"Error calculating video duration: {e}")
                finally:
                    fs.delete(fs.path(video_path))  
            else:
                video_file = Record_Class_Db.objects.get(id=upd_id).Upload_Class
                video_duration = Record_Class_Db.objects.get(id=upd_id).Video_Duration
        except Exception as e:
            print(f"Error handling video file: {e}")
            video_file = Record_Class_Db.objects.get(id=upd_id).Upload_Class
            video_duration = Record_Class_Db.objects.get(id=upd_id).Video_Duration

        try:
            pdf_file = request.FILES.get("S_Pdf_file_")
            if pdf_file:
                fs = FileSystemStorage()
                pdf_path = fs.save(pdf_file.name, pdf_file)
            else:
                pdf_path = Record_Class_Db.objects.get(id=upd_id).Upload_PDF
        except Exception as e:
            print(f"Error handling PDF file: {e}")
            pdf_path = Record_Class_Db.objects.get(id=upd_id).Upload_PDF

        Record_Class_Db.objects.filter(id=upd_id).update(Mentors_Id=Mentors_Id,Exam=exam,Course=course,Subject=subject,Topic_Name=topic_name,Description=description,Upload_Class=video_file,Upload_PDF=pdf_path,Video_Duration=video_duration,
        )
        return redirect("Upload_Record_Class")

# End Upload Class Details



