from django.urls import path
from . import views

urlpatterns = [
    path('Home_Page/',views.Home_Page,name='Home_Page'),
    path('About_Page/',views.About_Page,name='About_Page'),
    path('Contact_Page/',views.Contact_Page,name='Contact_Page'),
    path('Save_Contact/',views.Save_Contact,name='Save_Contact'),
    path('Course_Page/',views.Course_Page,name='Course_Page'),
    path('Subject_Page/',views.Subject_Page,name='Subject_Page'),
    path('Blog_page/',views.Blog_page,name='Blog_page'),
    path('View_Textbook_Page/',views.View_Textbook_Page,name='View_Textbook_Page'),
    path('View_Study_Material/',views.View_Study_Material,name='View_Study_Material'),
    path('View_Question_Paper/',views.View_Question_Paper,name='View_Question_Paper'),
    path('Edit_Profile/',views.Edit_Profile,name='Edit_Profile'),
    path('Chat_Page/',views.Chat_Page,name='Chat_Page'),
    path('Live_Class_Page/',views.Live_Class_Page,name='Live_Class_Page'),
    path('Mock_Test_Page/',views.Mock_Test_Page,name='Mock_Test_Page'),



]  