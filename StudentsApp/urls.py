from django.urls import path 
from . import views

urlpatterns = [
    path('Student_Register/',views.Student_Register,name='Student_Register'),
    path('Save_Student_Register/',views.Save_Student_Register,name='Save_Student_Register'),
    path('Student_LogIn/',views.Student_LogIn,name='Student_LogIn'),
    path('Save_Student_LogIn/',views.Save_Student_LogIn,name='Save_Student_LogIn'),
    path('Student_Logout/',views.Student_Logout,name='Student_Logout'),
    path('verify_otp/', views.Verify_OTP, name='verify_otp'),

    path('forgot_password/', views.ForgotPassword, name='forgot_password'),
    path('send_otp/', views.SendOTP, name='send_otp'),
    path('VerifyOTP/', views.VerifyOTP, name='VerifyOTP'),
    path('reset_password/', views.ResetPassword, name='reset_password'),

    path('group_chat/<str:course_name>/', views.group_chat, name='group_chat'),
    
    
    
]
 