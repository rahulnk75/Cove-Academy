from django.urls import path
from . import views

urlpatterns = [
    path('Courses_Filterd/<Cour_name>/',views.Courses_Filterd,name='Courses_Filterd'),
    path('Subject_Filterd/<sub_name>/<int:Ex_id>/',views.Subject_Filterd,name='Subject_Filterd'),
    path('Class_Page/<int:sub_id>/<int:sub_name_id>/',views.Class_Page,name='Class_Page'),
    path('Payment_Page/<int:pay_id>/',views.Payment_Page,name='Payment_Page'),
    path('Subject_Payment_Page/<int:pay_id>/',views.Subject_Payment_Page,name='Subject_Payment_Page'),
    path('Save_Payment_Page/',views.Save_Payment_Page,name='Save_Payment_Page'),
    path('Save_Subject_Payment_Page/',views.Save_Subject_Payment_Page,name='Save_Subject_Payment_Page'),


     

    

    


]  