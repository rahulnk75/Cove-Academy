from django.urls import path 
from . import views

urlpatterns = [
    path('Student_Register/',views.Student_Register,name='Student_Register'),
    path('Save_Student_Register/',views.Save_Student_Register,name='Save_Student_Register'),
    path('Student_LogIn/',views.Student_LogIn,name='Student_LogIn'),
    path('Save_Student_LogIn/',views.Save_Student_LogIn,name='Save_Student_LogIn'),
    path('Student_Logout/',views.Student_Logout,name='Student_Logout'),
    path('OTP_page/',views.OTP_page,name='OTP_page')
    
    
]
 