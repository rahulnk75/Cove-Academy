from django.urls import path 
from . import views

urlpatterns = [ 
    path('Mentors_Home_Page/',views.Mentors_Home_Page,name='Mentors_Home_Page'),
# start Mentors details
    path('Mentors_Login/',views.Mentors_Login,name='Mentors_Login'),
    path('Mentors_Register/',views.Mentors_Register,name='Mentors_Register'),
    path('Save_Mentors_Register/',views.Save_Mentors_Register,name='Save_Mentors_Register'),
    path('Save_Mentors_Login/',views.Save_Mentors_Login,name='Save_Mentors_Login'),
    path('Mentors_Logout/',views.Mentors_Logout,name='Mentors_Logout'),
    path('Verify_OTP_/', views.Verify_OTP_, name='Verify_OTP_'),
    path('Mentors_Edit_Profile/', views.Mentors_Edit_Profile, name='Mentors_Edit_Profile'),
    # Mentor Forgotpassword
    path('forgotpassword/', views.Mentors_ForgotPassword, name='mentors_forgotpassword'),
    path('sendotp/', views.Mentors_SendOTP, name='mentors_sendotp'),
    path('verifyotp/', views.Mentors_VerifyOTP, name='mentors_verifyotp'),
    path('resetpassword/', views.Mentors_ResetPassword, name='mentors_resetpassword'),
    # Mentor register OTP
    path('mentors_forgot-password/', views.Mentors_ForgotPassword, name='Mentors_ForgotPassword'),
    path('mentors_send-otp/', views.Mentors_SendOTP, name='Mentors_SendOTP'),
    path('mentors_verify-otp/', views.Mentors_VerifyOTP, name='Mentors_VerifyOTP'),
    path('mentors_reset-password/', views.Mentors_ResetPassword, name='Mentors_ResetPassword'),
# End Mentors details

# Start Text Book Details
    path('Add_Textbook_Page/',views. Add_Textbook_Page,name='Add_Textbook_Page'),
    path('Display_Textbook/',views. Display_Textbook,name='Display_Textbook'),
    path('Save_Textbook/',views. Save_Textbook,name='Save_Textbook'),
    path('Download_PDF_Textbook/<pk>/',views. Download_PDF_Textbook,name='Download_PDF_Textbook'),
    path('Delete_Textbook/<int:del_id>/',views. Delete_Textbook,name='Delete_Textbook'),
    path('Edit_Textbook/<int:edit_id>/',views.Edit_Textbook,name='Edit_Textbook'),
    path('Upload_Textbook/<int:upd_id>/',views.Upload_Textbook,name='Upload_Textbook'),
# End Text Book Details

# Start Study material Details
    path('Add_Study_Material/',views.Add_Study_Material,name='Add_Study_Material'),
    path('Display_Study_Material/',views.Display_Study_Material,name='Display_Study_Material'),
    path('Save_Study_Material/',views.Save_Study_Material,name='Save_Study_Material'),
    path('Download_PDF_Study_Material/<pk>/',views. Download_PDF_Study_Material,name='Download_PDF_Study_Material'),
    path('Delete_Study_Material/<int:del_id>/',views. Delete_Study_Material,name='Delete_Study_Material'),
    path('Edit_Study_Material/<int:edit_id>/',views.Edit_Study_Material,name='Edit_Study_Material'),
    path('Upload_Study_Material/<int:upd_id>/',views.Upload_Study_Material,name='Upload_Study_Material'),
# End Study material Details

# Start Question Paper Details
   path('Add_Question_Paper/',views.Add_Question_Paper,name='Add_Question_Paper'),
   path('Display_Question_Paper/',views.Display_Question_Paper,name='Display_Question_Paper'),
   path('Save_Question_Paper/',views.Save_Question_Paper,name='Save_Question_Paper'),
   path('Download_PDF_Question_Paper/<pk>/',views. Download_PDF_Question_Paper,name='Download_PDF_Question_Paper'),
   path('Delete_Question_Paper/<int:del_id>/',views. Delete_Question_Paper,name='Delete_Question_Paper'),
   path('Edit_Question_Paper/<int:edit_id>/',views.Edit_Question_Paper,name='Edit_Question_Paper'),
   path('Upload_Question_Paper/<int:upd_id>/',views.Upload_Question_Paper,name='Upload_Question_Paper'),
# End Question Paper Details   

# Start Upload Class Details
   path('Upload_Record_Class/',views.Upload_Record_Class,name='Upload_Record_Class'),
   path('get-courses-by-exam/', views.get_courses_by_exam, name='get_courses_by_exam'),
   path('get-subjects-by-course/', views.get_subjects_by_course, name='get_subjects_by_course'),
   path('Save_upload_record_class/',views.Save_upload_record_class,name='Save_upload_record_class'),
   path('Display_Rcecord_Class/',views.Display_Rcecord_Class,name='Display_Rcecord_Class'),
   path('Download_PDF_Rcecord_Class/<pk>/',views. Download_PDF_Rcecord_Class,name='Download_PDF_Rcecord_Class'),
   path('Delete_Rcecord_Class/<int:del_id>/',views. Delete_Rcecord_Class,name='Delete_Rcecord_Class'),
   path('Edit_Rcecord_Class/<int:edit_id>/',views.Edit_Rcecord_Class,name='Edit_Rcecord_Class'),
   path('Upload_Upload_Record_Class/<int:upd_id>/',views.Upload_Upload_Record_Class,name='Upload_Upload_Record_Class'),
# End Upload Class Details

]
